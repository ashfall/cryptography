


# 'leaf' certificate is a certificate with CA: false

class Certificate(object):
    def get_asn1_bytes():
        """
        Get the ASN1-format bytes of the certificate.
        """


class ClientCertificateStore(object):
    def get_certificate_chain_for_roots(roots, certificate_chain_callback):
        """
        This method is intended to be implemented by the user, NOT called by
        the user.

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

    def get_default_certificate_chain(certificate_chain_callback):
        """
        This method is intended to be implemented by the user, NOT called by the
        user.

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
    """
    def __init__(certificates):
        """
        @param certificates: A set of Certificate objects, none of which may
            have private keys. If any private keys are found in any of the
            certificates, an error will be raised.
        """



