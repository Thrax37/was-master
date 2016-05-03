local datas={}
local arg=arg[1]..";"

-- parse the arguments
-- add some meta datas for debuging purpose/usefulness
arg:gsub("(.-);",function(c)
  if not datas.round
  then
    datas.round=c+0
  elseif not datas.myID
  then
    datas.myID=c+0
  elseif not datas.coins
  then
    datas.coins=c+0
  else
    datas[#datas+1]={}
    datas[#datas].repr=c
    c=c.."_"
    tmp={}
    c:gsub("(.-)_",function(d) tmp[#tmp+1]=d end)
    datas[#datas].id=tmp[1]+0
    datas[#datas].points=tmp[2]+0
    datas[#datas].flip=tmp[3]+0
    datas[#datas].unflip=tmp[4]+0
    if datas[#datas].id==datas.myID
    then
      datas.myOrder=#datas
      datas.myDatas=datas[#datas]
    end
  end
end)

local actions=""
-- construct actions
for i=1,3
do
  -- if we aren't in balance and can grab more coins
  -- we do it
  if #actions==0 and datas.myDatas.unflip<=datas.myDatas.flip/2 and datas.coins>=3
  then
    actions=actions.."3"
    datas.myDatas.unflip=datas.myDatas.unflip+3
    datas.coins=datas.coins-3
  -- if we couldn't grab coins, but aren't in balance, we flip some coins
  elseif datas.myDatas.unflip>datas.myDatas.flip/2
  then
    actions=actions.."F"
    datas.myDatas.unflip=datas.myDatas.unflip-1
    datas.myDatas.flip=datas.myDatas.flip+1

  -- if we didn't have anything to do on our pile, let's punish
  -- the fools who doesn't follow the great Balance principle
  else
    previous=datas.myOrder<2 and #datas or datas.myOrder-1
    following=datas.myOrder>=#datas and 1 or datas.myOrder+1

    lossPrev=-datas[previous].flip + 2*datas[previous].unflip
    lossFoll=-datas[following].flip+ 2*datas[following].unflip
    if lossFoll>0 and lossPrev>0
    then
      actions =actions.."N"
    elseif lossFoll>=lossPrev
    then
      actions=actions.."T"
      datas[following].unflip,datas[following].flip=datas[following].flip,datas[following].unflip
    else
      actions=actions.."R"
      datas[previous].unflip,datas[previous].flip=datas[previous].flip,datas[previous].unflip
    end
  end
end
print(actions)