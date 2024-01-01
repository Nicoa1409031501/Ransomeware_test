import time

def stage1():
    # 第一階段的程式碼
    print("Executing stage 1...")
    time.sleep(3)

def stage2():
    # 第二階段的程式碼
    print("Executing stage 2...")
    time.sleep(3)

def stage3():
    # 第三階段的程式碼
    print("Executing stage 3...")
    time.sleep(3)

def execute_multi_stage():
    # 呼叫多階段的程式碼
    stage1()
    stage2()
    stage3()
    print("Multi-stage execution completed.")

execute_multi_stage()