# Statistics
> :timer_clock: Last update: 02/02/2025 at 01:09:16 - Domains analyzed count: 150000.

> :mag_right: View the markdown code to see the exact percentage because mermaid use integer values for rendering.

## Global usage of secure headers

Provide the distribution of usage of secure headers across all domains analyzed.

```mermaid
pie
	"Not using them" : 26.17
	"Using them" : 73.83

```


## Global usage of header 'cache-control'

Provide the distribution of usage of the header 'cache-control' across all domains analyzed.

```mermaid
pie
	"Using it" : 60.3
	"Not using it" : 39.7

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
	"Using it" : 18.82
	"Not using it" : 81.18

```


## Global usage of header 'content-security-policy-report-only'

Provide the distribution of usage of the header 'content-security-policy-report-only' across all domains analyzed.

```mermaid
pie
	"Using it" : 1.5
	"Not using it" : 98.5

```


## Global usage of header 'cross-origin-embedder-policy'

Provide the distribution of usage of the header 'cross-origin-embedder-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 4.67
	"Not using it" : 95.33

```


## Global usage of header 'cross-origin-opener-policy'

Provide the distribution of usage of the header 'cross-origin-opener-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 5.92
	"Not using it" : 94.08

```


## Global usage of header 'cross-origin-resource-policy'

Provide the distribution of usage of the header 'cross-origin-resource-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 5.07
	"Not using it" : 94.93

```


## Global usage of header 'expect-ct'

Provide the distribution of usage of the header 'expect-ct' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.9
	"Not using it" : 99.1

```


## Global usage of header 'feature-policy'

Provide the distribution of usage of the header 'feature-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.97
	"Not using it" : 99.03

```


## Global usage of header 'permissions-policy'

Provide the distribution of usage of the header 'permissions-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 8.85
	"Not using it" : 91.15

```


## Global usage of header 'public-key-pins'

Provide the distribution of usage of the header 'public-key-pins' across all domains analyzed.

```mermaid
pie
	"Using it" : 0.07
	"Not using it" : 99.93

```


## Global usage of header 'referrer-policy'

Provide the distribution of usage of the header 'referrer-policy' across all domains analyzed.

```mermaid
pie
	"Using it" : 21.31
	"Not using it" : 78.69

```


## Global usage of header 'strict-transport-security'

Provide the distribution of usage of the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 35.57
	"Not using it" : 64.43

```


## Global usage of header 'x-content-type-options'

Provide the distribution of usage of the header 'x-content-type-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 32.74
	"Not using it" : 67.26

```


## Global usage of header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed.

```mermaid
pie
	"Using it" : 37.59
	"Not using it" : 62.41

```


## Global usage of header 'x-permitted-cross-domain-policies'

Provide the distribution of usage of the header 'x-permitted-cross-domain-policies' across all domains analyzed.

```mermaid
pie
	"Using it" : 3.84
	"Not using it" : 96.16

```


## Global usage of header 'x-xss-protection'

Provide the distribution of usage of the header 'x-xss-protection' across all domains analyzed.

```mermaid
pie
	"Using it" : 21.82
	"Not using it" : 78.18

```


## Global usage of insecure framing configuration via the header 'x-frame-options'

Provide the distribution of usage of the header 'x-frame-options' across all domains analyzed with a insecure framing configuration: value different from `DENY` or `SAMEORIGIN` including unsupported values.

```mermaid
pie
	"Insecure conf" : 2.29
	"Secure conf" : 97.71

```


## Global usage of insecure referrer configuration via the header 'referrer-policy'

Provide the distribution of usage of the header 'referrer-policy' across all domains analyzed with a insecure referrer configuration: value set to `unsafe-url` or `no-referrer-when-downgrade`.

`no-referrer-when-downgrade` was included because it send origin, path, and querystring when the protocol security level stays the same (HTTPS is very often in place).

```mermaid
pie
	"Insecure conf" : 4.34
	"Secure conf" : 95.66

```


## Global usage of the Strict Transport Security 'preload' feature

Provide the distribution of usage of the '[preload](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security#preloading_strict_transport_security)' feature for the header 'strict-transport-security' across all domains analyzed.

```mermaid
pie
	"Using it" : 25.4
	"Not using it" : 74.6

```


## Global common 'max-age' values of the Strict Transport Security header

* Most common value used is 31536000 seconds (525600 minutes) across all domains analyzed.
* Maximum value used is 1234513412313 seconds (20575223539 minutes) across all domains analyzed.
* Minimum value used is -5375190 seconds (-89586 minutes) across all domains analyzed.


## Global usage of content security policy with directives allowing unsafe expressions

Provide the distribution of content security policy allowing unsafe expressions across all domains analyzed.

Determine if a CSP policy contains `(default-src|script-src|script-src-elem|script-src-attr|style-src)` directives using `(unsafe-inline|unsafe-hashes|unsafe-eval)` expressions.

Based on [Report-URI CSP](https://report-uri.com/home/generate) generator allowed instructions for CSP directives.

```mermaid
pie
	"Using unsafe" : 7.65
	"Not using unsafe" : 92.35

```

