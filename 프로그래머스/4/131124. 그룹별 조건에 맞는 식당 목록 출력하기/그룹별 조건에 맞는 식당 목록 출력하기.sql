-- 코드를 입력하세요
select p.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d')
from rest_review r join (select p.member_name, p.member_id
                        from member_profile p join (SELECT member_id, count(*) as cnt
                                                    from rest_review
                                                    group by member_id
                                                    order by cnt desc
                                                    limit 1) m on p.member_id = m.member_id) p
                                                    on r.member_id = p.member_id
order by r.review_date, r.review_text