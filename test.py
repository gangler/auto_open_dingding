import uiautomator2 as u2
import threading
import schedule
import time


def auto_open_app():
    d.app_start("com.alibaba.android.rimet")
    d(className="android.widget.RelativeLayout", instance=13).click()
    # sess = d.session("com.alibaba.android.rimet")
    # sess(className="android.widget.RelativeLayout", instance=13).click()
    print("OK!")


if __name__ == '__main__':
    d = u2.connect('192.168.0.110')
    print(d.info)
    # 检查并维持设备端守护进程处于运行状态
    # thread = threading.Thread(target=d.healthcheck())
    # thread.setDaemon(True)
    # thread.start()
    schedule.every(10).seconds.do(auto_open_app)
    while True:
        schedule.run_pending()
        time.sleep(1)




