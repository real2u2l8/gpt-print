#GPT Header - sector 1
# 1. offset 72byte 8byte = partition Entries Strating
# 2. 120byte 기준으로 파티션 엔트리가 갈라짐 -> 파티션 갯수 세기
# 3. 파티션엔트리가 없다고 판단 될때 (0x00 1byte 확인하기)
# 4. partition entry 중 offset 16byte -> guid,
#   32Byte 파티션 시작 LBA, 그다음 8byte가 끝나는 LBA 위치
#   둘이 빼서 크기 구하기
# 파일시스템타입(guid,hexa 대문자)		실시작오프셋		파티션사이즈
import sys

def caclPartSize(): # 파티션 사이즈 계산
    return True

def checkNoEntry(): #파티션 엔트리 없는지체크
    return True

def lba2rvaH(): #rva = ((byteorder)lba->Dec * 512)-> hex
    return True

def printEntries(): ## 파티션 엔트리 출력
    return True



if __name__ == '__main__' :
    if len(sys.argv) == 1 :
        print("Usage : gpt-analyzer.py <gpt.dd>")    
    elif len(sys.argv) < 3:
        print("Usage : gpt-analyzer.py <gpt.dd>")
        print("Usage : only one argument")
       
    file_path = sys.argv[1]
