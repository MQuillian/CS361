# CookieMicroservice

<u>Making a Request</u>
To make a request to the Cookie Microservice, send an HTTP request to the following address:
{hostname}:8001/get_cookie?darkmode={value}

NOTES:
* The hostname will depend on the hosting method selected. Should the microservice be hosted on a web hosting platform, then the hostname will correspond to that platform. If Docker is chosen, then the hostname will correspond to the Docker container in which the program is running.
* The value assigned to the darkmode query parameter is not checked or interpreted by the microservice. It is intended as a boolean, but the Cookie Microservice is not dependent on the manner in which the boolean is set. Thus, the caller may set whatever value it wishes and must be prepared to properly interpret that value once it is set in the cookie.

<u>Receiving a Response</u>
To receive the response from the Cookie Microservice, simply check the HTTP response that is sent back after making a request. The cookie may be found in the Set-Cookie portion of the response header.
The cookie name is simply 'cookie' and the value is a JSON string that contains the userid and darkmode values. An example JSON string is as follows:
"userid": AjsJgh35has, "darkmode": False

NOTES:
* The userid value will be a randomized, 12 character alphanumeric string
* The darkmode value will be whatever value was contained in the query parameter received in the request

<u>Diagram</u>

![MicroserviceDiagram](https://github.com/MQuillian/CS361/assets/38482544/5e04e2a8-9f93-4b2d-acf5-c2f3a5250854)
