import sys,getopt
from datetime import datetime, date, timedelta, time

def set_env(argv):

    # 初始化参数
    region_id = ''
    secret_id = ''
    secret_key = ''
    endpoint = ''
    product_name = 'ecs'
    api = ''
    filename = ''
    start_time = (datetime.today() + timedelta(days = -1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    last_time = datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")

    # 配置选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:u:k:f:s:l:",["region_id=","secret_id=","secret_key=","endpoint=","api=",
                                   "filename=","start_time=","last_time="])

    # 处理异常
    except getopt.GetoptError:
        print("""
        script.py -r <region_id> -u <secret_id> -k <secret_key> <endpoint> <api> -f <filename> -s <start_time> -l <last_time>
        """)
        sys.exit(2)

    # 传递参数
    for opt, arg in opts:
        if opt == "-h":
            print("""
            script.py -r <region_id> -u <secret_id> -k <secret_key> <endpoint> <api> -f <filename> -s <start_time> -l <last_time>
            """)
            sys.exit(2)
        elif opt in ("-r", "--region_id"):
            region_id = arg
        elif opt in ("-u", "--secret_id"):
            secret_id = arg
        elif opt in ("-k", "--secret_key"):
            secret_key = arg
        elif opt in ("--endpoint"):
            endpoint = arg
        elif opt in ("--api"):
            api = arg
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-s", "--start_time"):
            start_time = arg
        elif opt in ("-l", "--last_time"):
            last_time = arg
    return (region_id, secret_id, secret_key, endpoint, product_name, api, filename, start_time, last_time)

#if __name__ == "__main__":
#    set_env(sys.argv[1:])
