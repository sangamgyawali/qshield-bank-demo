"""TLS transport configuration for the core banking API gateway."""
import ssl


def build_server_context(cert_path: str, key_path: str) -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_path, key_path)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    return context
