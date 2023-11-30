Table of Contents
URL (Uniform Resource Locator)
HTTP (Hypertext Transfer Protocol)
Reading a URL
HTTP URL Scheme
Domain Name
Sub-Domain
Port Number in a URL
Query String
HTTP Request
HTTP Response
HTTP Headers
HTTP Message Body
HTTP Request Method
HTTP Response Status Code
HTTP Cookie
Making a Request with cURL
Typing "google.com" in Your Browser
URL (Uniform Resource Locator)
A URL is a web address used to identify and locate resources on the internet. It consists of several components, including the scheme, domain name, path, query parameters, and fragment.

HTTP (Hypertext Transfer Protocol)
HTTP is a protocol used for communication between web browsers and web servers. It defines how requests and responses are formatted and transmitted, enabling the retrieval of resources such as HTML files, images, and more.

Reading a URL
A URL can be read from left to right, starting with the scheme (e.g., "http" or "https"), followed by the domain name, path, query parameters, and fragment.

HTTP URL Scheme
The scheme in an HTTP URL indicates the protocol being used, such as "http" or "https." It defines how the resource will be accessed and transmitted.

Domain Name
A domain name is a human-readable label used to identify a specific location on the internet. It typically consists of a recognizable name followed by a top-level domain (TLD), like ".com," ".org," or ".net."

Sub-Domain
A sub-domain is a prefix added to a domain name, creating a more specific web address. For instance, "blog.example.com" is a sub-domain of "example.com."

Port Number in a URL
A port number can be specified in a URL to indicate the specific communication endpoint on the server. It follows the domain name and is preceded by a colon (e.g., "http://example.com:8080").

Query String
The query string appears after the path in a URL and is used to send additional information to the server. It consists of key-value pairs separated by "&" and is often used in GET requests.

HTTP Request
An HTTP request is sent by a client (e.g., a web browser) to a server, asking for a specific resource. It contains information such as the request method, headers, and, in some cases, a message body.

HTTP Response
An HTTP response is the server's reply to an HTTP request. It includes a status code indicating the success or failure of the request, along with headers and a response body containing the requested resource.

HTTP Headers
HTTP headers provide additional information about the request or response. They include metadata such as content type, content length, and authentication credentials.

HTTP Message Body
The HTTP message body carries the data being sent in the request or response. It's used to transmit content like the payload of a POST request or the content of a web page.

HTTP Request Method
The HTTP request method specifies the intended action for the server. Common methods include GET (retrieve), POST (send data), PUT (update), and DELETE (remove).

HTTP Response Status Code
The HTTP response status code indicates the outcome of an HTTP request. Examples include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).

HTTP Cookie
An HTTP cookie is a small piece of data sent from the server and stored in the client's browser. It's often used to track user sessions and store user preferences.

Making a Request with cURL
cURL is a command-line tool for making HTTP requests. It allows you to specify the request method, headers, data, and more, directly from the terminal.
Typing "google.com" in Your Browser
When you type "google.com" in your browser and hit Enter, your browser initiates an HTTP GET request to the server hosting Google's website. The server responds with an HTML file, which your browser renders and displays as the Google homepage..
