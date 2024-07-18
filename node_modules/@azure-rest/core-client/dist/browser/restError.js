// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.
import { RestError, createHttpHeaders } from "@azure/core-rest-pipeline";
export function createRestError(messageOrResponse, response) {
    var _a;
    const resp = typeof messageOrResponse === "string" ? response : messageOrResponse;
    const internalError = resp.body.error || resp.body;
    const message = typeof messageOrResponse === "string"
        ? messageOrResponse
        : (_a = internalError.message) !== null && _a !== void 0 ? _a : `Unexpected status code: ${resp.status}`;
    return new RestError(message, {
        statusCode: statusCodeToNumber(resp.status),
        code: internalError.code,
        request: resp.request,
        response: toPipelineResponse(resp),
    });
}
function toPipelineResponse(response) {
    var _a;
    return {
        headers: createHttpHeaders(response.headers),
        request: response.request,
        status: (_a = statusCodeToNumber(response.status)) !== null && _a !== void 0 ? _a : -1,
    };
}
function statusCodeToNumber(statusCode) {
    const status = Number.parseInt(statusCode);
    return Number.isNaN(status) ? undefined : status;
}
//# sourceMappingURL=restError.js.map