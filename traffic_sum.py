import os

# 文件格式如下
# t=1692499311,d=baidu.com,r=sichuan,i=china-telecom,a=A,c_req=0,c_resp=0,c_req_s=18508,c_resp_s=5289746,ch_hit=0,ch_miss=0,ch_hit_s=0,ch_miss_s=5289746,p_req=0,p_resp=0,s_req=7628,s_resp=6295490,s_req_s=0,s_resp_s=0,code=206:6
def get_all_files(path):
    files = []
    for f in os.listdir(path):
        file_name = os.path.join(path, f)
        files.append(file_name)
    return files


def parse_file(file_name):
    traffic_sum = 0
    file_handle = open(file_name, "r")
    lines = file_handle.readlines()
    for l in lines:
        ln = l.strip("\n")  # 去掉换行符号
        line_dict = parse_line(ln)
        if len(line_dict):
            if line_dict['d'] == "baidu.com" and line_dict['a'] == "A":
                c_resp = int(line_dict["c_resp"])
                c_resp_s = int(line_dict["c_resp_s"])
                sum_resp = c_resp + c_resp_s
                traffic_sum += sum_resp
    return traffic_sum


def parse_line(line):
    line_dict = {}
    lines = line.split(",")
    for l in lines:
        kv = l.split("=")
        if len(kv):
            try:
                line_dict[kv[0]] = kv[1]
            except:
                print("catch error", lines)
    return line_dict


if __name__ == '__main__':
    dir_path = "/users/file/log"
    files = get_all_files(dir_path)
    sum = 0
    for f in files:
        traffic = parse_file(f)
        sum += traffic

    print(sum)
