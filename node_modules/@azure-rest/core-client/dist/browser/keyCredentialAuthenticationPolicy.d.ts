import { KeyCredential } from "@azure/core-auth";
import { PipelinePolicy } from "@azure/core-rest-pipeline";
/**
 * The programmatic identifier of the bearerTokenAuthenticationPolicy.
 */
export declare const keyCredentialAuthenticationPolicyName = "keyCredentialAuthenticationPolicy";
export declare function keyCredentialAuthenticationPolicy(credential: KeyCredential, apiKeyHeaderName: string): PipelinePolicy;
//# sourceMappingURL=keyCredentialAuthenticationPolicy.d.ts.map