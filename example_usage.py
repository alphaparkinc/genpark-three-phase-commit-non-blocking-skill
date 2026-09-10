from client import ThreePhaseCommit

class Mock3PCParticipant:
    def __init__(self):
        self.state = "INIT"
    def can_commit(self, tx_id): return True
    def pre_commit(self, tx_id): self.state = "PRECOMMIT"
    def do_commit(self, tx_id): self.state = "COMMITTED"
    def abort(self, tx_id): self.state = "ABORTED"

def main():
    print("=== Testing Three-Phase Commit Protocol ===")
    parts = [Mock3PCParticipant(), Mock3PCParticipant()]
    tpc = ThreePhaseCommit(parts)
    ok, st = tpc.execute("tx_3pc_001")
    print("3PC execution status:", st)

    assert ok and st == "COMMITTED_3PC"
    assert all(p.state == "COMMITTED" for p in parts)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
