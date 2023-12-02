# Statistics
> :timer_clock: Last update: 12/02/2023 at 00:52:00 - Domains analyzed count: 200000.

> :mag_right: View the markdown code to see the exact percentage because mermaid use integer values for rendering.

## Global usage of secure headers

Provide the distribution of usage of secure headers across all domains analyzed.

```mermaid
pie
	"Not using them" : 37.27
	"Using them" : 62.73

```


## Global usage of header 'cache-control'

Provide the distribution of usage of the header 'cache-control' across all domains analyzed.

```mermaid
pie
	"Using it" : 50.68
	"Not using it" : 49.32

```


## Global usage of header 'clear-site-data'

Provide the distribution of usage of the header 'clear-site-data' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.01
	"Not using it" : 99.99

```


## Global usage of header 'content-security-policy'

Provide the distribution of usage of the header 'content-security-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 14.53
	"Not using it" : 85.47

```


## Global usage of header 'content-security-policy-report-only'

Provide the distribution of usage of the header 'content-security-policy-report-only' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.16
	"Not using it" : 98.84

```


## Global usage of header 'cross-origin-embedder-policy'

Provide the distribution of usage of the header 'cross-origin-embedder-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.25
	"Not using it" : 98.75

```


## Global usage of header 'cross-origin-opener-policy'

Provide the distribution of usage of the header 'cross-origin-opener-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.96
	"Not using it" : 98.05

```


## Global usage of header 'cross-origin-resource-policy'

Provide the distribution of usage of the header 'cross-origin-resource-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.52
	"Not using it" : 98.48

```


## Global usage of header 'expect-ct'

Provide the distribution of usage of the header 'expect-ct' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.73
	"Not using it" : 99.27

```


## Global usage of header 'feature-policy'

Provide the distribution of usage of the header 'feature-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.87
	"Not using it" : 99.13

```


## Global usage of header 'permissions-policy'

Provide the distribution of usage of the header 'permissions-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 4.21
	"Not using it" : 95.79

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
	"Using it" : 13.19
	"Not using it" : 86.81

```


## Global usage of header 'strict-transport-security'

Provide the distribution of usage of the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 29.2
	"Not using it" : 70.8

```


## Global usage of header 'x-content-type-options'

Provide the distribution of usage of the header 'x-content-type-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 28.16
	"Not using it" : 71.84

```


## Global usage of header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 28.92
	"Not using it" : 71.08

```


## Global usage of header 'x-permitted-cross-domain-policies'

Provide the distribution of usage of the header 'x-permitted-cross-domain-policies' across all domains analyzed.

```mermaid
pie
	"Using it" : 3.44
	"Not using it" : 96.56

```


## Global usage of header 'x-xss-protection'

Provide the distribution of usage of the header 'x-xss-protection' across all domains analyzed.

```mermaid
pie
	"Using it" : 20.02
	"Not using it" : 79.98

```


## Global usage of insecure framing configuration via the header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed with a insecure framing configuration: value different from `DENY` or `SAMEORIGIN` including unsupported values.

```mermaid
pie
	"Insecure conf" : 2.02
	"Secure conf" : 97.98

```


## Global usage of insecure referrer configuration via the header 'referrer-policy'

Provide the distribution of usage of the header 'referrer-policy' across all domains analyzed with a insecure referrer configuration: value set to `unsafe-url` or `no-referrer-when-downgrade`.

`no-referrer-when-downgrade` was included because it send origin, path, and querystring when the protocol security level stays the same (HTTPS is very often in place).

```mermaid
pie
	"Insecure conf" : 4.04
	"Secure conf" : 95.96

```


## Global usage of the Strict Transport Security 'preload' feature

Provide the distribution of usage of the '[preload](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security#preloading_strict_transport_security)' feature for the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 21.67
	"Not using it" : 78.33

```


## Global common 'max-age' values of the Strict Transport Security header

* Most common value used is 31536000 seconds (525600 minutes) across all domains analyzed.
* Maximum value used is 1234513412313 seconds (20575223539 minutes) across all domains analyzed.
* Minimum value used is -384394633 seconds (-6406577 minutes) across all domains analyzed.


## Global usage of content security policy with directives allowing unsafe expressions

Provide the distribution of content security policy allowing unsafe expressions across all domains analyzed.

Determine if a CSP policy contains `(default-src|script-src|script-src-elem|script-src-attr|style-src)` directives using `(unsafe-inline|unsafe-hashes|unsafe-eval)` expressions.

Based on [Report-URI CSP](https://report-uri.com/home/generate) generator allowed instructions for CSP directives.

```mermaid
pie
	"Using unsafe" : 5.78
	"Not using unsafe" : 94.22

```

