from enum import Enum

class ResponseCode(Enum):
    # Informational responses
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102

    # Success responses
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    ALREADY_REPORTED = 208
    IM_USED = 226

    # Redirection messages
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308

    # Client error responses
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    # Server error responses
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    NOT_EXTENDED = 510
    NETWORK_AUTHENTICATION_REQUIRED = 511

    @classmethod
    def get_message(cls, code):
        return {
            cls.CONTINUE: "Continue",
            cls.SWITCHING_PROTOCOLS: "Switching Protocols",
            cls.PROCESSING: "Processing",
            cls.OK: "OK",
            cls.CREATED: "Created",
            cls.ACCEPTED: "Accepted",
            cls.NON_AUTHORITATIVE_INFORMATION: "Non-Authoritative Information",
            cls.NO_CONTENT: "No Content",
            cls.RESET_CONTENT: "Reset Content",
            cls.PARTIAL_CONTENT: "Partial Content",
            cls.MULTI_STATUS: "Multi-Status",
            cls.ALREADY_REPORTED: "Already Reported",
            cls.IM_USED: "IM Used",
            cls.MULTIPLE_CHOICES: "Multiple Choices",
            cls.MOVED_PERMANENTLY: "Moved Permanently",
            cls.FOUND: "Found",
            cls.SEE_OTHER: "See Other",
            cls.NOT_MODIFIED: "Not Modified",
            cls.USE_PROXY: "Use Proxy",
            cls.TEMPORARY_REDIRECT: "Temporary Redirect",
            cls.PERMANENT_REDIRECT: "Permanent Redirect",
            cls.BAD_REQUEST: "Bad Request",
            cls.UNAUTHORIZED: "Unauthorized",
            cls.PAYMENT_REQUIRED: "Payment Required",
            cls.FORBIDDEN: "Forbidden",
            cls.NOT_FOUND: "Not Found",
            cls.METHOD_NOT_ALLOWED: "Method Not Allowed",
            cls.NOT_ACCEPTABLE: "Not Acceptable",
            cls.PROXY_AUTHENTICATION_REQUIRED: "Proxy Authentication Required",
            cls.REQUEST_TIMEOUT: "Request Timeout",
            cls.CONFLICT: "Conflict",
            cls.GONE: "Gone",
            cls.LENGTH_REQUIRED: "Length Required",
            cls.PRECONDITION_FAILED: "Precondition Failed",
            cls.PAYLOAD_TOO_LARGE: "Payload Too Large",
            cls.URI_TOO_LONG: "URI Too Long",
            cls.UNSUPPORTED_MEDIA_TYPE: "Unsupported Media Type",
            cls.RANGE_NOT_SATISFIABLE: "Range Not Satisfiable",
            cls.EXPECTATION_FAILED: "Expectation Failed",
            cls.IM_A_TEAPOT: "I'm a teapot",
            cls.MISDIRECTED_REQUEST: "Misdirected Request",
            cls.UNPROCESSABLE_ENTITY: "Unprocessable Entity",
            cls.LOCKED: "Locked",
            cls.FAILED_DEPENDENCY: "Failed Dependency",
            cls.TOO_EARLY: "Too Early",
            cls.UPGRADE_REQUIRED: "Upgrade Required",
            cls.PRECONDITION_REQUIRED: "Precondition Required",
            cls.TOO_MANY_REQUESTS: "Too Many Requests",
            cls.REQUEST_HEADER_FIELDS_TOO_LARGE: "Request Header Fields Too Large",
            cls.UNAVAILABLE_FOR_LEGAL_REASONS: "Unavailable For Legal Reasons",
            cls.INTERNAL_SERVER_ERROR: "Internal Server Error",
            cls.NOT_IMPLEMENTED: "Not Implemented",
            cls.BAD_GATEWAY: "Bad Gateway",
            cls.SERVICE_UNAVAILABLE: "Service Unavailable",
            cls.GATEWAY_TIMEOUT: "Gateway Timeout",
            cls.HTTP_VERSION_NOT_SUPPORTED: "HTTP Version Not Supported",
            cls.VARIANT_ALSO_NEGOTIATES: "Variant Also Negotiates",
            cls.INSUFFICIENT_STORAGE: "Insufficient Storage",
            cls.LOOP_DETECTED: "Loop Detected",
            cls.NOT_EXTENDED: "Not Extended",
            cls.NETWORK_AUTHENTICATION_REQUIRED: "Network Authentication Required",
        }.get(code, "Unknown Status Code")
