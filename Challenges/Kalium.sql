create table noOverlaps
( 
    startLine int,
    endLine int
);


insert into noOverlaps
select 
    outOne.l as startLine, 
    outOne.r as endLine 
from 
    segments as outOne
where
    not exists (
                    select *
                    from segments as inner
                    where
                        outOne.l>=inner.l
                        and outOne.r<=inner.r
                        and (outOne.l<>inner.l or outOne.r<> inner.r)
                )
order by startLine asc;


select
(
    select 
        IFNULL(sum(endLine - startLine),0)
    from
        noOverlaps
)
+
(
    select 
        IFNULL(sum(secondOne.startLine - firstOne.endLine),0)
    from
        noOverlaps as firstOne
        ,noOverlaps as secondOne
    where
        firstOne.startLine <= secondOne.startLine
        and firstOne.endLine >= secondOne.startLine
        and (firstOne.startLine <> secondOne.startLine or firstOne.endLine <> secondOne.endLine)
        and secondOne.startLine = (
                                    select 
                                        min(thirdOne.startLine)
                                    from 
                                        noOverlaps as thirdOne
                                    where
                                        thirdOne.startLine >= firstOne.startLine
                                        and (thirdOne.startLine <> firstOne.startLine or thirdOne.endLine <> thirdOne.endLine)
                                    )
);
