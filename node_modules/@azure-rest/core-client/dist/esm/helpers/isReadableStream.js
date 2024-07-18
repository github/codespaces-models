// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.
/**
 * Checks if the body is a ReadableStream supported by Node
 * @internal
 */
export function isReadableStream(body) {
    return Boolean(body) && typeof body.pipe === "function";
}
//# sourceMappingURL=isReadableStream.js.map