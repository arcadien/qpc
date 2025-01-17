# test-script for QUTest unit testing harness
# see https://www.state-machine.com/qtools/qutest.html/qutest.html

# preamble
def on_reset():
    expect_pause()

def Q_PRIO(prio, pthre):
    return prio | (pthre << 8)

test("ao->ao->ao (NO PTS)")
current_obj(OBJ_AP, "pspecB")
poke(0, 2, pack("<HHH", Q_PRIO(1,0), Q_PRIO(2,0), Q_PRIO(3,0)))
continue_test()
expect_run()
#----
glb_filter(GRP_SC, GRP_UA)
current_obj(OBJ_AO, "aoB[1]")
post("TEST0_SIG")
expect("@timestamp Sch-Next Pri=0->2")
expect("@timestamp CONTEXT_SW NULL aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST0 1of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[2] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST0 2of2")
expect("@timestamp TRACE_MSG aoB[1] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp Sch-Next Pri=1->3")
expect("@timestamp CONTEXT_SW aoB[0] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp Sch-Idle Pri=1->0")
expect("@timestamp CONTEXT_SW aoB[0] NULL")
expect("@timestamp Trg-Done QS_RX_EVENT")


test("ao->ao->ao (PTS1)")
current_obj(OBJ_AP, "pspecB")
poke(0, 2, pack("<HHH", Q_PRIO(1,3), Q_PRIO(2,3), Q_PRIO(3,0)))
continue_test()
expect_run()
#----
glb_filter(GRP_SC, GRP_UA)
current_obj(OBJ_AO, "aoB[1]")
post("TEST0_SIG")
expect("@timestamp Sch-Next Pri=0->2")
expect("@timestamp CONTEXT_SW NULL aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST0 1of2")
expect("@timestamp TRACE_MSG aoB[1] TEST0 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[2] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[1] TEST1 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[0] TEST1 2of2")
expect("@timestamp Sch-Next Pri=1->3")
expect("@timestamp CONTEXT_SW aoB[0] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp Sch-Idle Pri=1->0")
expect("@timestamp CONTEXT_SW aoB[0] NULL")
expect("@timestamp Trg-Done QS_RX_EVENT")


test("ao->ao->ao (PTS2)")
current_obj(OBJ_AP, "pspecB")
poke(0, 2, pack("<HHH", Q_PRIO(1,0), Q_PRIO(2,3), Q_PRIO(3,0)))
continue_test()
expect_run()
#----
glb_filter(GRP_SC, GRP_UA)
current_obj(OBJ_AO, "aoB[1]")
post("TEST0_SIG")
expect("@timestamp Sch-Next Pri=0->2")
expect("@timestamp CONTEXT_SW NULL aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST0 1of2")
expect("@timestamp TRACE_MSG aoB[1] TEST0 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[2] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[1] TEST1 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp Sch-Next Pri=1->3")
expect("@timestamp CONTEXT_SW aoB[0] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp Sch-Idle Pri=1->0")
expect("@timestamp CONTEXT_SW aoB[0] NULL")
expect("@timestamp Trg-Done QS_RX_EVENT")


test("ao->ao->ao (PTS2, NORESET)", NORESET)
post("TEST0_SIG")
expect("@timestamp Sch-Next Pri=0->2")
expect("@timestamp CONTEXT_SW NULL aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST0 1of2")
expect("@timestamp TRACE_MSG aoB[1] TEST0 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[2] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp TRACE_MSG aoB[1] TEST1 2of2")
expect("@timestamp Sch-Next Pri=2->3")
expect("@timestamp CONTEXT_SW aoB[1] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 1of2")
expect("@timestamp Sch-Lock Ceil=0->3")
expect("@timestamp Sch-Unlk Ceil=3->0")
expect("@timestamp Sch-Next Pri=1->3")
expect("@timestamp CONTEXT_SW aoB[0] aoB[2]")
expect("@timestamp TRACE_MSG aoB[2] TEST2 1of1")
expect("@timestamp Sch-Next Pri=3->2")
expect("@timestamp CONTEXT_SW aoB[2] aoB[1]")
expect("@timestamp TRACE_MSG aoB[1] TEST2 1of1")
expect("@timestamp Sch-Next Pri=2->1")
expect("@timestamp CONTEXT_SW aoB[1] aoB[0]")
expect("@timestamp TRACE_MSG aoB[0] TEST1 2of2")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp TRACE_MSG aoB[0] TEST2 1of1")
expect("@timestamp Sch-Idle Pri=1->0")
expect("@timestamp CONTEXT_SW aoB[0] NULL")
expect("@timestamp Trg-Done QS_RX_EVENT")

