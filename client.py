class ThreePhaseCommit:
    """
    Three-Phase Commit (3PC) Non-Blocking Transaction Protocol.
    Eliminates coordinator single-point-of-failure deadlocks.
    """
    def __init__(self, participants):
        self.participants = participants

    def execute(self, tx_id):
        for p in self.participants:
            if not p.can_commit(tx_id):
                for part in self.participants:
                    part.abort(tx_id)
                return False, "ABORTED_CAN_COMMIT"

        for p in self.participants:
            p.pre_commit(tx_id)

        for p in self.participants:
            p.do_commit(tx_id)
        return True, "COMMITTED_3PC"
