def parse_student(line):
    fields = line.strip().split(",")

    if len(fields) != 2:
        raise ValueError("字段数量必须为2")

    name = fields[0].strip()
    score_text = fields[1].strip()

    if name == "":
        raise ValueError("姓名不能为空")

    try:
        score = int(score_text)
    except ValueError:
        raise ValueError("成绩必须能转换为整数") from None

    if not 0 <= score <= 100:
        raise ValueError("成绩必须在0～100之间")

    return {"name": name, "score": score}