# Iteratively expand and search the chemical space of a tail structure递归在尾部骨架生成完整尾部
* This script was being written and used when I was assigned to explore the chemical space of certain tails.
* By defining tail structure and use this script, it will eventually give different tail length combinations of the origin tail structure, with names like "TailA_CxCyCz". TailA is the name of the origin tail structure. CxCyCz means TailA has 3 subtails and x, y, z are lengths of each subtail.
* The subtail length can be defined with tail_ranges.
* It is a fast and convenient way to expand chemical space of a tail structure.

```py
cstring = 'CCCCCCCCCCC'

expand_tails = {}

for name, tailscaf in name2tailscaf.items():  # name2tailscaf is a dict where the keys are tail's name, values are SMILES tails.
    num_tails = len(tailscaf) # 动态计算需要生成的tail数
    tail_ranges = [range(0, 4)] + [range(0, 10)] * (num_tails - 1)  # 定义subtail的长度范围, the first subtail is from 0 to 3, and the others from 0 to 9 (it actually turns out to be 1-4 and 1-10)

    # 使用递归生成所有可能的tail组合
    def generate_tails(index=0, current_tails=[]):
        if index == num_tails:  # 如果所有的tail都生成完毕
            # 拼接结果
            newtail = ''.join(tailscaf[i] + current_tails[i] for i in range(len(tailscaf)))
            name_newtail = name+'_'+''.join(f"C{len(s)+1}" for s in current_tails)
            expand_tails[name_newtail] = newtail
#             print(f"New tail for {name_newtail}: {newtail}")  # 或者将结果存储起来
            return

        # 遍历当前tail的长度范围
        for length in tail_ranges[index]:
            new_tail = cstring[:length]
            generate_tails(index + 1, current_tails + [new_tail])  # 递归生成下一个tail

    # 开始递归生成
    generate_tails()
    print('Finished ',name)
    print('Tails now:',len(expand_tails))

tail_df = pd.DataFrame(expand_tails,index=['tail.slice.SMILES']).T
tail_df.reset_index(inplace = True)
tail_df.rename(columns = {"index":"Tail_ID"},inplace = True)

```


