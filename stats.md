# Statistics
> :timer_clock: Last update: 08/03/2024 at 15:55:00 - Domains analyzed count: 150000.

> :mag_right: View the markdown code to see the exact percentage because mermaid use integer values for rendering.

## Global usage of secure headers

Provide the distribution of usage of secure headers across all domains analyzed.

```mermaid
pie
	"Not using them" : 52.64
	"Using them" : 47.36

```


## Global usage of header 'cache-control'

Provide the distribution of usage of the header 'cache-control' across all domains analyzed.

```mermaid
pie
	"Using it" : 37.71
	"Not using it" : 62.29

```


## Global usage of header 'clear-site-data'

Provide the distribution of usage of the header 'clear-site-data' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.0
	"Not using it" : 100.0

```


## Global usage of header 'content-security-policy'

Provide the distribution of usage of the header 'content-security-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 11.47
	"Not using it" : 88.53

```


## Global usage of header 'content-security-policy-report-only'

Provide the distribution of usage of the header 'content-security-policy-report-only' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.08
	"Not using it" : 98.92

```


## Global usage of header 'cross-origin-embedder-policy'

Provide the distribution of usage of the header 'cross-origin-embedder-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 2.28
	"Not using it" : 97.72

```


## Global usage of header 'cross-origin-opener-policy'

Provide the distribution of usage of the header 'cross-origin-opener-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 3.01
	"Not using it" : 96.99

```


## Global usage of header 'cross-origin-resource-policy'

Provide the distribution of usage of the header 'cross-origin-resource-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 2.57
	"Not using it" : 97.43

```


## Global usage of header 'expect-ct'

Provide the distribution of usage of the header 'expect-ct' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.56
	"Not using it" : 99.44

```


## Global usage of header 'feature-policy'

Provide the distribution of usage of the header 'feature-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.69
	"Not using it" : 99.31

```


## Global usage of header 'permissions-policy'

Provide the distribution of usage of the header 'permissions-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 4.77
	"Not using it" : 95.23

```


## Global usage of header 'public-key-pins'

Provide the distribution of usage of the header 'public-key-pins' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.04
	"Not using it" : 99.96

```


## Global usage of header 'referrer-policy'

Provide the distribution of usage of the header 'referrer-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 11.93
	"Not using it" : 88.07

```


## Global usage of header 'strict-transport-security'

Provide the distribution of usage of the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 24.25
	"Not using it" : 75.75

```


## Global usage of header 'x-content-type-options'

Provide the distribution of usage of the header 'x-content-type-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 20.59
	"Not using it" : 79.41

```


## Global usage of header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 22.92
	"Not using it" : 77.08

```


## Global usage of header 'x-permitted-cross-domain-policies'

Provide the distribution of usage of the header 'x-permitted-cross-domain-policies' across all domains analyzed.

```mermaid
pie
	"Using it" : 2.2
	"Not using it" : 97.8

```


## Global usage of header 'x-xss-protection'

Provide the distribution of usage of the header 'x-xss-protection' across all domains analyzed.

```mermaid
pie
	"Using it" : 14.0
	"Not using it" : 86.0

```


## Global usage of insecure framing configuration via the header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed with a insecure framing configuration: value different from `DENY` or `SAMEORIGIN` including unsupported values.

```mermaid
pie
	"Insecure conf" : 1.48
	"Secure conf" : 98.52

```


## Global usage of insecure referrer configuration via the header 'referrer-policy'

Provide the distribution of usage of the header 'referrer-policy' across all domains analyzed with a insecure referrer configuration: value set to `unsafe-url` or `no-referrer-when-downgrade`.

`no-referrer-when-downgrade` was included because it send origin, path, and querystring when the protocol security level stays the same (HTTPS is very often in place).

```mermaid
pie
	"Insecure conf" : 2.66
	"Secure conf" : 97.34

```


## Global usage of the Strict Transport Security 'preload' feature

Provide the distribution of usage of the '[preload](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security#preloading_strict_transport_security)' feature for the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 17.99
	"Not using it" : 82.01

```


## Global common 'max-age' values of the Strict Transport Security header

* Most common value used is 31536000 seconds (525600 minutes) across all domains analyzed.
* Maximum value used is 1234513412313 seconds (20575223539 minutes) across all domains analyzed.
* Minimum value used is -273748882 seconds (-4562481 minutes) across all domains analyzed.


## Global usage of content security policy with directives allowing unsafe expressions

Provide the distribution of content security policy allowing unsafe expressions across all domains analyzed.

Determine if a CSP policy contains `(default-src|script-src|script-src-elem|script-src-attr|style-src)` directives using `(unsafe-inline|unsafe-hashes|unsafe-eval)` expressions.

Based on [Report-URI CSP](https://report-uri.com/home/generate) generator allowed instructions for CSP directives.

```mermaid
pie
	"Using unsafe" : 4.99
	"Not using unsafe" : 95.01

```

