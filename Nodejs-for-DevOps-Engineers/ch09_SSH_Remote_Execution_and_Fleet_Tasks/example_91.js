// Book: Node.js for DevOps Engineers — Example 91
// src/fleet/sftp.js
export function upload(conn, local, remote) {
  return new Promise((resolve, reject) => {
    conn.sftp((err, sftp) => {
      if (err) return reject(err);
      sftp.fastPut(local, remote, (e) => {
        sftp.end();
        return e ? reject(e) : resolve();
      });
    });
  });
}
