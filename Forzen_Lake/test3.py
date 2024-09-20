import numpy as np
import gym
import time
import matplotlib.pyplot as plt
clsck = 0 
stps = [0,1,2,3,4,5,6,7]

no_of_steps = []

rewardss = []
no_of_epso = 0

y =[]
k = 0 

def render_single(env, policy, max_steps=7):
    global k 
    global step
    global net_reward 
    net_reward = 0
    step = 0 
    
    """
      This function does not need to be modified
      Renders policy once on environment. Watch your agent play!

      Parameters
      ----------
      env: gym.core.Environment
        Environment to play on. Must have nS, nA, and P as
        attributes.
      Policy: np.array of shape [env.nS]
        The action to take at a given state
    """
    episode_reward = 0

    ob = env.reset()
    ob = ob[0]            # Try this or Comment this based on [doing in Colab or VsCode]
    for t in range(max_steps):
        step+=1 
        env.render()
        time.sleep(0.25)
        a = policy[ob]
        print(a)
        ob, rew, done, _ ,_= env.step(int(a))
        net_reward+= rew 
        k+=1
         # remove a blank after done if on Colab 
       


        episode_reward += rew
        
        if done:
            break
    env.render()
    if not done:
        rewardss.append(net_reward)
        net_reward = 0 
        no_of_steps.append(100)
        step = 0 

       
        print("The agent didn't reach a terminal state in {} steps.".format(max_steps))
        
    else:
        no_of_steps.append(step)
        rewardss.append(net_reward)
        net_reward = 0 
        step = 0 

        print("Episode reward: %f" % episode_reward)
        
 




no_of_itraitons = 1000000
theta = 1e-8
gamma = 1
env = gym.make("FrozenLake-v1",is_slippery=False)
P = env.P
nS = 16
nA=4
lst2 = [] 

new = np.zeros(nS) 
V = np.zeros(nS)
act_poly = np.zeros(nS)



def calc_VF(V,P,state,action,gamma):
    global rewardss
    v = 0 
    for probablity,next_state,reward,terminal in P[state][action]:
        v+= probablity*(reward+gamma*(V[next_state]))

    return v


# POlicy evalution 


j = 0       
f= 0
alpha =0 
hss = [] 
while True: 
        while True:
            j += 1  
            delta = 0 
            for sts in range (nS):
                 v = V[sts]
                 V[sts]= calc_VF(V,P,sts,act_poly[sts],gamma)
                 delta = max(delta,abs(v-V[sts]))       
            if delta < theta: 
                break


        policy_stable = True
        for sts in range(nS):
           old_action = act_poly[sts]
           act_poly[sts] = np.argmax([calc_VF(V,P,sts,a,gamma)for a in range(nA)])
           if old_action != act_poly[sts]:
               policy_stable = False
        if policy_stable :
            break
        f+=1 
        
        print(act_poly)
        render_single(env,act_poly)
        hss.append(act_poly)



        
# print('Policy itration :: \n','Value Function ', V,'\n','Policy ', act_poly ,'\n')

    





V = np.zeros(nS)
actn_poly = np.zeros(nS)


i = 0 
while True:
    i += 1 
    delta = 0 
    for sts in range(nS):
        v = V[sts]
        lst1 = []           
        for action in range(nA) :
            vS = 0 
            for prob, nextstate,reward , ternimal in P[sts][action]:
                vS += prob*(reward + gamma*V[nextstate])
                
                
            lst1.append(vS)

        V[sts]= max(lst1)
 
        delta = max(delta,abs(v-V[sts]))


    if delta < theta :break

    actn_poly = np.zeros(nS)
    for sts in range(nS):
        vS = 0 
        va = new[sts]
        old_p = actn_poly[sts]
        lst1 = []
        for action in range(nA) :
            for prob, nextstate,reward , ternimal in P[sts][action]:
                vS += prob*(reward + gamma*V[nextstate])
            lst1.append(vS)
       
        actn_poly[sts] = np.argmax(lst1)







        

# print('Value Itration ::  ','\n','Value Function ', V ,'\n','Policy ', act_poly,'\n')

# generate returns --- > 


#Imps Codeeee

render_single(env,act_poly)
      

print(no_of_steps)     
print(stps)
print(rewardss)

plt.subplot(3, 1, 1)
plt.title("Gamma = 1 ")
plt.plot(stps,rewardss,color='g')
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.title("Rewards / Epsiode",loc="left")

plt.subplot(3, 1, 3)
plt.plot(stps,no_of_steps,color='r')
plt.title("No Of Steps / Epsiode",loc="left")
plt.xlabel("Episodes")
plt.ylabel("No_Of_Steps")
plt.show()
















        

    





                
    








