import json
import os
from datetime import datetime

MEMO_FILE = "memos.json"

def load_memos():
    """메모 파일에서 데이터 로드"""
    if os.path.exists(MEMO_FILE):
        with open(MEMO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_memos(memos):
    """메모 데이터를 파일에 저장"""
    with open(MEMO_FILE, "w", encoding="utf-8") as f:
        json.dump(memos, f, ensure_ascii=False, indent=2)

def create_memo(title, content):
    """새 메모 생성"""
    memos = load_memos()
    memo = {
        "id": len(memos) + 1,
        "title": title,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    memos.append(memo)
    save_memos(memos)
    print(f"✓ 메모가 생성되었습니다! (ID: {memo['id']})")

def view_all_memos():
    """모든 메모 보기"""
    memos = load_memos()
    if not memos:
        print("저장된 메모가 없습니다.")
        return
    
    print("
" + "="*60)
    for memo in memos:
        print(f"[ID: {memo['id']}] {memo['title']}")
        print(f"작성: {memo['created']}")
        print(f"내용: {memo['content'][:50]}...")
        print("-"*60)


def view_memo(memo_id):
    """특정 메모 보기"""
    memos = load_memos()
    for memo in memos:
        if memo["id"] == memo_id:
            print("
" + "="*60)
            print(f"[ID: {memo['id']}] {memo['title']}")
            print(f"작성: {memo['created']}")
            print(f"수정: {memo['updated']}")
            print("="*60)
            print(memo['content'])
            print("="*60 + "\n")
            return
    print(f"ID {memo_id}인 메모를 찾을 수 없습니다.")

def edit_memo(memo_id, new_title, new_content):
    """메모 수정"""
    memos = load_memos()
    for memo in memos:
        if memo["id"] == memo_id:
            memo["title"] = new_title
            memo["content"] = new_content
            memo["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_memos(memos)
            print(f"✓ 메모가 수정되었습니다! (ID: {memo_id})")
            return
    print(f"ID {memo_id}인 메모를 찾을 수 없습니다.")

def delete_memo(memo_id):
    """메모 삭제"""
    memos = load_memos()
    for i, memo in enumerate(memos):
        if memo["id"] == memo_id:
            title = memo["title"]
            memos.pop(i)
            save_memos(memos)
            print(f"✓ 메모가 삭제되었습니다! ({title})")
            return
    print(f"ID {memo_id}인 메모를 찾을 수 없습니다.")

def search_memo(keyword):
    """메모 검색"""
    memos = load_memos()
    results = [memo for memo in memos if keyword.lower() in memo["title"].lower() or keyword.lower() in memo["content"].lower()]
    
    if not results:
        print(f"'{keyword}'와 일치하는 메모가 없습니다.")
        return
    
    print(f"\n검색 결과: {len(results)}개 찾았습니다.\n" + "="*60)
    for memo in results:
        print(f"[ID: {memo['id']}] {memo['title']}")
        print(f"내용: {memo['content'][:50]}...")
        print("-"*60)

def main():
    """메인 메뉴"""
    while True:
        print("\n📝 메모장 앱")
        print("1. 새 메모 작성")
        print("2. 모든 메모 보기")
        print("3. 특정 메모 보기")
        print("4. 메모 수정")
        print("5. 메모 삭제")
        print("6. 메모 검색")
        print("7. 종료")
        
        choice = input("\n선택 (1-7): ").strip()
        
        if choice == "1":
            title = input("메모 제목: ").strip()
            content = input("메모 내용: ").strip()
            if title and content:
                create_memo(title, content)
            else:
                print("제목과 내용을 입력해주세요.")
        
        elif choice == "2":
            view_all_memos()
        
        elif choice == "3":
            try:
                memo_id = int(input("메모 ID: "))
                view_memo(memo_id)
            except ValueError:
                print("올바른 ID를 입력해주세요.")
        
        elif choice == "4":
            try:
                memo_id = int(input("수정할 메모 ID: "))
                new_title = input("새 제목: ").strip()
                new_content = input("새 내용: ").strip()
                if new_title and new_content:
                    edit_memo(memo_id, new_title, new_content)
                else:
                    print("제목과 내용을 입력해주세요.")
            except ValueError:
                print("올바른 ID를 입력해주세요.")
        
        elif choice == "5":
            try:
                memo_id = int(input("삭제할 메모 ID: "))
                delete_memo(memo_id)
            except ValueError:
                print("올바른 ID를 입력해주세요.")
        
        elif choice == "6":
            keyword = input("검색어: ").strip()
            if keyword:
                search_memo(keyword)
            else:
                print("검색어를 입력해주세요.")
        
        elif choice == "7":
            print("메모장을 종료합니다. 👋")
            break
        
        else:
            print("올바른 선택을 해주세요.")

if __name__ == "__main__":
    main()