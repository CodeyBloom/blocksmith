# Bitcoin in Python

This is a dead simple implementstion of the Bitcoin protocol in Python. I'm trying to build another app that lets common accounting software have a bitcoin native interface. As I was implementing a payment server I kept running into problems that I didn't know the best way to approach. To fix this I decided to write a simple implementation of the bitcoin protocol in python.

I know there are several implenetations of the bitcoin protocol in python. However the code in this project will look a bit different. The reason for that is that I am learning Rust as well, and would really like to do a similar project in Rust, but I'm not ready. So instead I will try to "think Rust" and "think Python" at the same time. I'll structure the code in this project in a similar way to Rust, following 3 principles:

1. Prefer @dataclasses wherever possible.
2. Type hints everywhere.
3. Prefer immutable data structures.
4. Practice code soundness (unintended states should not be representable).

In addition to code style, I will probably take the chance to practice writing more robust python than I'm usually required to (testing, error handling, etc.).
