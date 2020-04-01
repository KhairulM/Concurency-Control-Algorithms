from concurrency_control import ConcurrencyControl

def main() :
    cc = ConcurrencyControl("MVCC", "a.txt", 2)
    cc.run()

main()