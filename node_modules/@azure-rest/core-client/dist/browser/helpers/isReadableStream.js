// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.
/**
 * Checks if the body is a ReadableStream supported by browsers
 * @internal
 */
export function isReadableStream(body) {
    return Boolean(body &&
        typeof body.getReader === "function" &&
        typeof body.tee === "function");
}
//# sourceMappingURL=isReadableStream-browser.mjs.map