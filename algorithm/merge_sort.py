## 归并排序

def merge_sort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
        
        while i <len(left) :
            list[k]=left[i]
            i+=1
            k+=1

        while j <len(right) :
            list[k]=right[j]
            j+=1
            k+=1
        return list


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(merge_sort(a))