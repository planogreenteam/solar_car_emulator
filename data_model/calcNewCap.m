function [battCap,noPower] = calcNewCap(batteryCapacity,motorLoad_AH,solarPanelIn_AH,maxBatteryCapacity)
  % Calculate new Battery Capacity
  battCap = batteryCapacity - motorLoad_AH + solarPanelIn_AH;
  if (battCap <= 0) 
    noPower = 1;
  else
    noPower = 0;
  end 
  
  if (battCap > maxBatteryCapacity)
    battCap = maxBatteryCapacity;
  end
endfunction
