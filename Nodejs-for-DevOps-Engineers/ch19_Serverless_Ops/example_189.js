// Book: Node.js for DevOps Engineers — Example 189
// functions/tag-creator/logic.js
export function tagsFromEvent(detail) {
  if (detail?.eventName !== 'RunInstances') return null;
  const ids = detail.responseElements?.instancesSet?.items
    ?.map((i) => i.instanceId) ?? [];
  if (!ids.length) return null;
  return {
    ids,
    tags: [
      { Key: 'created-by',
        Value: (detail.userIdentity?.arn ?? 'unknown')
          .slice(0, 256) },
      { Key: 'created-at', Value: detail.eventTime },
    ],
  };
}
