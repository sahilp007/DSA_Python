# TLE
#
# for n in range(999):
#     end = int(n ** 0.5)
#     found = False
#     start = 0
#     while end > start:
#         mul = end ** 2 + start ** 2
#         if mul == n:
#             print("n = ", n,"| Pos at: ", end, " and ", start)
#             break
#         if mul > n:
#             end -= 1class rough{
#     public static void main(String[] args) {
#         String s = "codeleet";
#         int[] indices = {4,5,6,7,0,1,2,3};
#         int[] ans = new int[indices.length];
#         for (int index : indices) {
#             ans[indices[index]] = s.charAt(index);
#         }
#         String s1= "";
#         for (int i = 0; i < s.length(); i++) {
#             s1 += (char) ans[i];
#         }
#         System.out.println(s1);
#     }
# }
#         if mul < n:
#             start += 1

# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 1, 2, 3]
s = "codeleet"
indices = [4, 5, 6, 7, 0, 1, 2, 3]
ans = []

for i in range(len(indices)):
    ans.append('')
for index in range(len(indices)):
    ans[indices[index]] = s[index]

print(ans)
s = "".join(ans)
