import os
import json
import logging
import urllib3

_debug = bool(os.environ.get('DEBUG'))

_logger = logging.getLogger('HomeAssistant-SmartHome')
_logger.setLevel(logging.DEBUG if _debug else logging.INFO)

def lambda_handler(event, context):
    """Handle incoming Alexa directive."""
    
    # Log the incoming event for debugging
    _logger.debug('Received event: %s', json.dumps(event, indent=4))

    # Get the base URL from the environment variable
    base_url = os.environ.get('BASE_URL')
    assert base_url is not None, 'Please set BASE_URL environment variable'
    base_url = base_url.strip("/")

    # Get the directive from the event
    directive = event.get('directive')
    if directive is None:
        _logger.error('Malformatted request - missing directive')
        return {
            'event': {
                'payload': {
                    'type': 'INVALID_REQUEST',
                    'message': 'Missing directive'
                }
            }
        }

    # Log directive details for debugging
    _logger.debug('Directive details: %s', json.dumps(directive, indent=4))

    # Check payload version
    assert directive.get('header', {}).get('payloadVersion') == '3', \
        'Only support payloadVersion == 3'
    
    # Get the scope from the directive
    scope = directive.get('endpoint', {}).get('scope')
    if scope is None:
        scope = directive.get('payload', {}).get('grantee')
    if scope is None:
        scope = directive.get('payload', {}).get('scope')
    assert scope is not None, 'Malformatted request - missing endpoint.scope'
    assert scope.get('type') == 'BearerToken', 'Only support BearerToken'

    # Use hardcoded token here (replace with your token)
    token = 'TOKEN ICI'

    # SSL verification flag
    verify_ssl = not bool(os.environ.get('NOT_VERIFY_SSL'))
    
    # Create an HTTP client with the appropriate SSL configuration
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED' if verify_ssl else 'CERT_NONE',
        timeout=urllib3.Timeout(connect=2.0, read=10.0)
    )

    # Extract entity_id properly
    entity_id = directive.get('endpoint', {}).get('endpointId')
    _logger.debug('Extracted entity_id: %s', entity_id)

    # Ignore entity_id check for Discovery requests
    if directive.get('header', {}).get('namespace') != "Alexa.Discovery" and not entity_id:
        _logger.error('Entity ID missing in directive: %s', json.dumps(directive))
        return {
            'event': {
                'payload': {
                    'type': 'INVALID_REQUEST',
                    'message': 'Missing entity_id in directive'
                }
            }
        }

    # Make the request to Home Assistant
    response = http.request(
        'POST', 
        '{}/api/alexa/smart_home'.format(base_url),
        headers={
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json',
        },
        body=json.dumps(event).encode('utf-8'),
    )
    
    # Handle potential errors in the response
    if response.status >= 400:
        _logger.error('Error response from Home Assistant: %s', response.data.decode("utf-8"))
        return {
            'event': {
                'payload': {
                    'type': 'INVALID_AUTHORIZATION_CREDENTIAL' 
                            if response.status in (401, 403) else 'INTERNAL_ERROR',
                    'message': response.data.decode("utf-8"),
                }
            }
        }

    # Log the response from Home Assistant
    _logger.debug('Response from Home Assistant: %s', response.data.decode("utf-8"))
    
    # Return the response as JSON
    return json.loads(response.data.decode('utf-8'))
