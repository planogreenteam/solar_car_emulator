close all
clear all

maxBatteryCapacity = 10000; %mAh
batteryVoltage = 48; %Volts
hours = 10; % Hours for simulation
steps_hour = 60; % steps per hour

clear batteryCapacity;

batteryCapacity(1) = maxBatteryCapacity; % Initialize Battery Capacity

%% Set solarPanelIn_W to average input power per minute
solarPanelInput_FIXED = 100; %Watts

%% Set motorCurrent to average motor power per minute
motorCurrent = 10; %Amps

%% Fixed loading -- assumes fixed values from the top
motorLoad_A = repmat(motorCurrent,1,(hours*steps_hour)); % Conversion to Array
solarPanelIn_WH = repmat(solarPanelInput_FIXED,1,(hours*steps_hour)); % Conversion to Watt-Hours
batteryVoltage = repmat(48,1,(hours*steps_hour)); %Volts

%% We should create dummy motorload vectors, and solar panel vectors.
%% Also need to incorporate battery voltage variations.


for i = 1:hours*steps_hour
  
  % Convert Panel Wattage to Solar Panel Amps
  solarPanel_AH(i) = (solarPanelIn_WH(i) / batteryVoltage(i));
  
  % Convert Motor Loading to Amp Hours
  motorLoad_AH(i) = motorLoad_A(i);
  
  % Calculate new Battery Capacity
  if(i == 1) [batteryCapacity(i),noPower] = calcNewCap(maxBatteryCapacity,motorLoad_AH(i),solarPanel_AH(i),maxBatteryCapacity);
  else [batteryCapacity(i),noPower] = calcNewCap(batteryCapacity(i-1),motorLoad_AH(i),solarPanel_AH(i),maxBatteryCapacity);
  end
  
  if(noPower) 
    printf("No power at i = %d \n", i)
    break; 
  end
end

t = 1/steps_hour:1/steps_hour:hours;

subplot(3,1,1)
plot(t,motorLoad_AH);
axis('tight');
xlabel('Time (hour)');
ylabel('Motor Loading (Amp-Hr)')

subplot(3,1,2)
plot(t,solarPanel_AH.*batteryVoltage(1:size(solarPanel_AH,2)));
axis('tight');
xlabel('Time (hours)');
ylabel('Solar Panel Input (Watt-Hr)')

subplot(3,1,3)
plot(t,batteryCapacity);
axis('tight');
xlabel('Time (hours)');
ylabel('Battery Capacity (A-Hr) Remaining')