import sys
import json
from client import ThreePhaseCommit

class Simple3PC:
    def can_commit(self, tx): return True
    def pre_commit(self, tx): pass
    def do_commit(self, tx): pass
    def abort(self, tx): pass

def main():
    tpc = ThreePhaseCommit([Simple3PC(), Simple3PC()])
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "execute":
            ok, st = tpc.execute(params.get("tx_id", "tx_default"))
            res = {"success": ok, "status": st}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
