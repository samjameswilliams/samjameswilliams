# Pump suction  

On more than one occasion I've heard people say something like "you don't need to worry about friction or minor losses in the pump suction line". The truth is that you get exactly the same kind of head losses in suction pipe as any other pipe. The reason I think people get blase about pump suction pipe is that for many pump systems in the water industry, you can get away with ignoring the losses. Submersible pumps (almost) do away with the issue, and many suction lines are short. Factors of safety also cover up some design omissions.  

For some systems however, suction losses are significant and ignoring them could lead to selecting a pump that won't hit the design flow or deliver any flow at all, or might cause excessive cavitation and shake itself to pieces.  

The work a pump does in suction needs to be looked at in a different way to the work it does in discharge but the work is real. If you have a drink in a cup and you suck it through a wide straw, it's easier than if you suck it through a narrow straw.  

## Conceptualising suction  

Something I find useful is to conceptualise suction not as a pump pulling fluid into it, but as atmospheric pressure pushing the fluid in. Since atmospheric pressure is approximately equal to 1bar and 10m of water creates approximately 1bar pressure, it is physically impossible to lift water more than 10m in suction. There are reasons that even a hypothetical, perfect pump which could create a total vacuum at the suction, couldn't achieve a 10m lift.  

Normally engineers in the water industry like to use gauge pressure (e.g. barg) where 0 is atmospheric pressure. When thinking about suction it is very helpful to switch to absolute pressure where 0 is total vacuum.  

Another analogy I find useful is to think of the fluid as a chain of finite strength. You pull too hard and the chain breaks. The breaking point of a liquid is its vapour pressure. The vapour pressure is affected by the type of liquid and its temperature. If the pressure in the suction pipe drops below the liquid's vapour pressure, you break the chain, the liquid vaporises (boils) and that's cavitation. Cavitation is generally pretty undesirable because the bubbles of gas cause quite substantial forces as they appear and again as they collapse and this can cause damage. So, you have to subtract the water's vapour pressure from the 10m theoretical lift limitation. This is around 0.2m at normal UK temperatures.  

(These two analogies aren't exactly compatible but taken together I find them useful.)  

I'm rounding things off but to keep things simple,  let's say atmospheric pressure is exactly equal to 10m water pressure and water vapour pressure is exactly equal to 0.2m. Could a perfect pump lift 9.8m? No, why not? Because of the phenomenon some engineers ignore at their peril, head loss. The suction pipe for our hypothetical scenario needs to be at least 9.8m long, there will be some head loss at the inlet, friction losses from the pipe walls and possibly other minor losses. Those losses would drop the pressure in the water below its vapour pressure. Head losses in suction pipe are calculated in exactly the same way as for discharge pipe.  

## Positive displacement pumps  

Positive displacement pumps come in many varieties but they all share in common the trait that if you hold the pump still, there isn't a clear passage through the pump i.e. if you had a fish, no matter how small, it wouldn't be able to find a way to swim through. The fluid upstream is completely cut off from the fluid downstream.  

The suction lift capability of a positive displacement pump (or the suction head required) is basically a function of the pump's power and the quality of its seals. It is to be expected and anticipated that a positive displacement pump's suction lift capability will diminish over time as it wears and gaskets perish. If air is allowed in, or if water can pass from the discharge side to the suction side, this will mean the pump cannot drop the pressure quite so low at the suction end of the pump.  

## Rotodynamic pumps  

Rotodynamic pumps, in contrast to positive displacement pumps, do have a clear passage through the pump. They  work very much like propellers on a propeller aircraft but in a pump it's an impeller, not a propeller. For rotodynamic pumps the suction lift capability, or suction head required is more complicated. It depends on the flow rate through the pump and is published by the pump manufacturer as the NPSHr (net positive suction head required) curve. The NPSHr curve changes with the motor speed in the same way as the performance curve.    

What is common to both types is that they both lower the pressure of the fluid on the suction side (which draws the fluid into the pump), and raise the pressure on the discharge side (which propels the fluid down the discharge pipe).  

## Calculating the suction head available  

The formula for calculating the NPSHa (net positive suction heat available) is;  

$NPSHa = H_{st} - H_L + H_{atm} - H_{vap}$  

Where;  
$H_{st}$ is the static head = elevation of free water surface at the upstream end of the suction pipe - pump centreline elevation. This is negative if the pump is above the waterline.  

$H_L$ is the total head loss in the suction pipe (friction and minor losses)  
Alternatively you can combine $H_{st} - H_L$ and think of them together as the hydraulics grade line (HGL) at the pump intake. This is useful when you don't have a straightforward suction line (i.e. a booster pump in a network).  

$H_{atm}$ is atmospheric pressure.  

$H_{vap}$ is the vapour pressure of the liquid.  

If the NPSHa > NPSHr then the pump should be fine. However, it is prudent to use factors of safety to allow for uncertainty in the calculations and for pump wear. WIMES recommends  using the greater of 2m + NPSHr or 1.3 x NPSHr instead of the published NPSHr.  

The formula above occasionally gives the surprising result that a submersible pump, underwater, won't have sufficient NPSHa. This is most likely to happen if the pump is running towards the right of its curve and the level in the well has dropped low.  

The suction calculations also need to feed into the discharge calculations because the pump isn't just lifting from the upstream water level to the discharge level, you need to subtract the head losses in the suction pipe from the upstream level.  

I hope this is useful and shows why you shouldn't just ignore the suction losses when looking at pumped systems.