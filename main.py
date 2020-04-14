import Dev_tools
while True:
    # 显示功能菜单
    Dev_tools.show_menu()
    action_str = input("请选择希望执行的操作")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对系统的操作
    if action_str in ["1", "2", "3"]:
        # 新增设备
        if action_str == "1":
            Dev_tools.new_dev()
        # 显示全部设备
        elif action_str == "2":
            Dev_tools.show_alldev()
        # 查询设备
        elif action_str == "3":
            Dev_tools.search_dev()
    # 0 退出系统
    elif action_str == "0":
        print("将退出系统，欢迎再次使用！")
        break
    # 其他内容输入错误，需提示用户
    else:
        # 输入错误
        print("您输入的不正确，请重新选择！")


