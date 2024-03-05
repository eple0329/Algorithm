select ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPER_INFOS
where SKILL_3 = "Python" or SKILL_2 = "Python" or SKILL_1 = "Python"
order by ID asc