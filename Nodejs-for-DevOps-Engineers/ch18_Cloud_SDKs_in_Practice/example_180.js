// Book: Node.js for DevOps Engineers — Example 180
// src/cloud/aws/upload.js
import { createReadStream } from 'node:fs';
import { S3Client } from '@aws-sdk/client-s3';
import { Upload } from '@aws-sdk/lib-storage';

export async function uploadFile(bucket, key, file) {
  const upload = new Upload({
    client: new S3Client({}),
    params: {
      Bucket: bucket, Key: key,
      Body: createReadStream(file),
      ServerSideEncryption: 'aws:kms',
    },
    queueSize: 4,
    partSize: 16 * 1024 * 1024,
  });
  upload.on('httpUploadProgress', (p) => {
    if (p.total) {
      const pct = ((p.loaded / p.total) * 100).toFixed(0);
      process.stderr.write(`\r${pct}%`);
    }
  });
  await upload.done();
  process.stderr.write('\n');
}
