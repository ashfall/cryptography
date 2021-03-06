# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

import six

from cryptography import utils
from cryptography.exceptions import (
    AlreadyFinalized, UnsupportedAlgorithm, _Reasons
)
from cryptography.hazmat.backends.interfaces import HashBackend
from cryptography.hazmat.primitives import interfaces


@utils.register_interface(interfaces.HashContext)
class Hash(object):
    def __init__(self, algorithm, backend, ctx=None):
        if not isinstance(backend, HashBackend):
            raise UnsupportedAlgorithm(
                "Backend object does not implement HashBackend",
                _Reasons.BACKEND_MISSING_INTERFACE
            )

        if not isinstance(algorithm, interfaces.HashAlgorithm):
            raise TypeError("Expected instance of interfaces.HashAlgorithm.")
        self.algorithm = algorithm

        self._backend = backend

        if ctx is None:
            self._ctx = self._backend.create_hash_ctx(self.algorithm)
        else:
            self._ctx = ctx

    def update(self, data):
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized")
        if isinstance(data, six.text_type):
            raise TypeError("Unicode-objects must be encoded before hashing")
        self._ctx.update(data)

    def copy(self):
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized")
        return Hash(
            self.algorithm, backend=self._backend, ctx=self._ctx.copy()
        )

    def finalize(self):
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized")
        digest = self._ctx.finalize()
        self._ctx = None
        return digest


@utils.register_interface(interfaces.HashAlgorithm)
class SHA1(object):
    name = "sha1"
    digest_size = 20
    block_size = 64


@utils.register_interface(interfaces.HashAlgorithm)
class SHA224(object):
    name = "sha224"
    digest_size = 28
    block_size = 64


@utils.register_interface(interfaces.HashAlgorithm)
class SHA256(object):
    name = "sha256"
    digest_size = 32
    block_size = 64


@utils.register_interface(interfaces.HashAlgorithm)
class SHA384(object):
    name = "sha384"
    digest_size = 48
    block_size = 128


@utils.register_interface(interfaces.HashAlgorithm)
class SHA512(object):
    name = "sha512"
    digest_size = 64
    block_size = 128


@utils.register_interface(interfaces.HashAlgorithm)
class RIPEMD160(object):
    name = "ripemd160"
    digest_size = 20
    block_size = 64


@utils.register_interface(interfaces.HashAlgorithm)
class Whirlpool(object):
    name = "whirlpool"
    digest_size = 64
    block_size = 64


@utils.register_interface(interfaces.HashAlgorithm)
class MD5(object):
    name = "md5"
    digest_size = 16
    block_size = 64
