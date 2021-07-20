# Protected Services

#### Related Evolution Proposals
- [0317: SDL Protocol Security Specification](https://github.com/smartdevicelink/sdl_evolution/blob/master/proposals/0317-sdl-protocol-security-specification.md)

## 1. Overview

The authentication is done using TLS handshake. The TLS handshake process is defined by TLS and is not part of the SDL protocol.

## 2. Peer roles during the handshake

The handshake is designed as a client-server communication which is configurable in the system settings. An application must take the role of a server where the system is the client. The client entity will initiate a TLS handshake with the corresponding security manager of the server. The client will do this only if the server was not authenticated before in the current transport connection.

### 2.1 Peer certificate verification

According to the TLS handshake process the peer certificate can be omitted for the server but it's required for the client. Certificate peer verification can be enabled/disabled on the Core side by changing `VerifyPeer` parameter in the configuration file. On the other hand, the SDL app library does not require the certificate from Core for the TLS handshake. However, Core performs its internal certificate validation before starting the actual TLS handshake. During internal validation, Core checks if the certificate is missing (or outdated/invalid) and if so, it initiates a PTU to obtain a new certificate from the Policy Server. If a valid certificate can't be obtained, Core does not start the TLS handshake and it notifies the app library that the protected service start has failed.

## 3. RPC processing
After the [encryption of RPC service](https://github.com/smartdevicelink/sdl_overview_guides/blob/master/docs/RPC%20Encryption/index.md) is enabled, SDL Core rejects any unencrypted RPC requests with result code `ENCRYPTION_NEEDED` with the unencrypted response if the RPC needs protection. 

!!! NOTE

- SDL Core continues processing an unencrypted RPC request if the RPC does not need protection and responds with an unencrypted response.

- SDL Core continues processing an encrypted RPC request if the RPC needs protection and responds with an encrypted response.

- SDL Core sends an unencrypted notification if the RPC does not need protection.  

- SDL Core sends an encrypted notification if the RPC needs protection. In addition, SDL Core shall continue processing an encrypted RPC request if the RPC does not need protection and responds with an encrypted response.

!!!
