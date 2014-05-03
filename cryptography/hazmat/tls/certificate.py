from abc import ABCMeta, abstractmethod


# 'leaf' certificate is a certificate with CA: false

class Certificate(object):
    def get_asn1_bytes(self):
        """
        Get the ASN1-format bytes of the certificate.
        """


class ClientCertificateStore(object):
    def get_certificate_chain_for_roots(self, roots,
                                        certificate_chain_callback):
        """
        Get the client certificate chain to send to the server, based on the
        roots specified by the server.

        @param roots: A set of keyless certificates that the server specified
            as the valid roots that a client certificate must chain to.

        @param certificate_chain_callback: The callback that this method should
            eventually invoke to specify the client certificates to send. It
            must be passed either a single certificate chain (with ONE keyed
            leaf), or None to indicate no client certificates are available.
            The certificates must chain to one of the roots specified by the
            server.
        """

    def get_default_certificate_chain(self, certificate_chain_callback):
        """
        Get the default client certificate in the case that the server did not
        provide roots that the client certificate must chain to.

        @param certificate_chain_callback: The callback that this method should
            eventually invoke to specify the client certificates to send.  It
            must be passed either a single certificate chain (with ONE keyed
            leaf), or None to indicate no client certificates are available.
        """


class TrustStore(object):
    """
    Create a store of trusted CA certificates to be used with ClientTLS. No
    methods are public.

    If any private keys are found in any of the certificates,
    `ExtraneousPrivateKeyError` will be raised.
    """
    def __init__(self, certificates):
        """
        @param certificates: A set of Certificate objects, none of which may
            have private keys. If any private keys are found in any of the
            certificates, an error will be raised.
        """


class ServerCertificates(metaclass=ABCMeta):
    """
    An abstract base class representing the type of operations possible on a
    collection of server certificates.
    """
    @abstractmethod
    def get_certificate_chain_for_server_name(self, server_name,
                                              certificate_chain_callback):
        """
        Get the server chain to send to the client when the client is using
        Server Name Indication (SNI).

        @param server_name: The server name.

        @param certificate_chain_callback: A callable of one argument that
            must be eventually called by this method.
        """


class ServerCertificateChain(ServerCertificates):
    """
    Specify the certificate chain that will be sent to all clients.
    """
    def __init__(self, chain):
        """
        @param chain: A single chain of certificates, the leaf of which must
            have a private key.
        """


class SNIServerCertificates(ServerCertificates):
    """
    Represents a SNI-capable set of certificates for use with ServerTLS.
    """
    def __init__(self, certificates, default):
        """
        @param certificates: A set of certificates that may contain multiple
            distinct certificate chains. Any leaf certificates MUST have
            private keys.

        @param default: A single certificate chain, the leaf of which MUST have
            a private key.
        """
