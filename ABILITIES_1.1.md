# Creator expansion abilities — 1.1

100 plant-only additions and 100 zombie-only additions. The original 210 recipes remain shared, giving each maker 310 choices and the project 410 distinct abilities.

Amount = recipe damage/amount; Count = recipe burst/count; range and interval remain per-recipe settings. Conditional abilities wait until their documented conditions are met. Summons and grafts use your own selected templates. No gameplay presets are included.

## Plant abilities

| # | Ability | Category | Mechanic |
|---|---|---|---|
| 1 | Trellis intersections | Geometry | Strike enemies in the caster’s column OR lane; enemies at the intersection take both hits. |
| 2 | Checkerboard pulse | Geometry | Damage only enemies on the opposite tile parity to the caster. Each cast flips the chosen parity. |
| 3 | Expanding petal rings | Geometry | Three delayed damage rings expand from the caster at radii 100, 200 and 300; each ring hits only its band. |
| 4 | Bookend needles | Geometry | Strike the leftmost and rightmost enemies in range; if there is only one, hit it once for double damage. |
| 5 | Diagonal lattice | Geometry | Strike enemies whose row distance equals their column distance from the caster, excluding its own tile. |
| 6 | Zigzag bloom trail | Geometry | A column-by-column pulse alternates between the lane above and below the caster. Count sets the number of columns. |
| 7 | Border vine strike | Geometry | Hit enemies occupying the outermost rows or first/last columns. Interior enemies are untouched. |
| 8 | Forked lane current | Geometry | Hit one enemy in each adjacent lane; if both forks find a target, also strike every enemy between their columns in the caster lane. |
| 9 | Comb-tooth volley | Geometry | Fire from alternating columns ahead of the caster rather than from the plant. Count limits the teeth. |
| 10 | Spiral tile sequence | Geometry | Walk clockwise through the eight tiles surrounding the caster, striking a different tile every quarter second. |
| 11 | Sun escrow | Economy | Store up to Amount loose banked sun. The next activation returns the deposit doubled only if no zombie has entered this lane’s first two columns. |
| 12 | Sun denomination split | Economy | Split the largest nearby sun token into Count+1 equal-value tokens. Total value stays unchanged and expiry resets. |
| 13 | Duplicate packet coupon | Economy | Pay Amount sun to make the caster’s own packet free twice; cannot stack while either coupon remains. |
| 14 | Sun route | Economy | Move every loose sun token to a line just behind the caster and extend its life by two seconds. No auto-collection. |
| 15 | Terrain dividend | Economy | Earn Amount divided by ten for each different terrain type currently present on the lawn. |
| 16 | Rain savings barrel | Economy | During rain or storms, bank one charge each cast. In other weather release all stored charges as Amount-sun tokens, up to ten. |
| 17 | Seed auction | Economy | Sell the oldest conveyor packet for its template cost or Amount, whichever is lower. Conveyor only. |
| 18 | Maturing sunlight | Economy | Tag nearby loose sun: each gains Amount after three seconds if still uncollected. Each token matures only once. |
| 19 | Frugal planting streak | Economy | Arm a six-second streak: each consecutive planting costing no more than the previous earns Amount sun. An expensive purchase breaks the streak. |
| 20 | Sundial advance | Economy | Bring the next sky-sun drop forward by Amount/10 seconds. Any time already due instead refreshes the caster packet recharge. |
| 21 | Recipe timer relay | Support | Move up to Amount/10 seconds from the caster’s slowest other timer to the nearest ally’s slowest timer. |
| 22 | Rotating triage | Support | Heal one different injured ally each cast; do not repeat an ally until every eligible ally has been treated. |
| 23 | Paired roots | Support | Bind the two lowest-health allies for six seconds; each second, transfer excess health from the healthier percentage to the weaker without creating health. |
| 24 | Cross-pollination | Support | Allies with a different template from the caster gain temporary shields; matching templates instead advance their timers by one second. |
| 25 | Range graft | Support | Temporarily extend every recipe range on the nearest other ally by Amount, capped at 1500. Original values return after six seconds. |
| 26 | Nursery ward | Support | For six seconds, newly planted allies in range receive Amount shield and one second of stun protection. |
| 27 | Prismatic guard | Support | Count allies receive a shield that blocks the next damage event of a different recipe type from the one last blocked. |
| 28 | Shared sun pulse | Support | Collect the smallest loose sun token; heal each ally by its value divided among them and advance packet recharge by value/25 seconds. |
| 29 | Veteran instruction | Support | An older caster lends Amount armor percentage points to younger allies for five seconds; does not affect peers or older plants. |
| 30 | Guard rotation | Support | Move the largest active allied shield to the weakest ally and refresh its lifetime. Shield points are conserved. |
| 31 | Stretching tripwire | Traps | Create a wire between caster and target. For five seconds enemies crossing its original midpoint are rooted and hit once. |
| 32 | Pressure plate quorum | Traps | Place a trap at the target tile. It detonates only when Count+1 enemies share its radius, for Amount per enemy. |
| 33 | Sticky sap meter | Traps | Coat a target for six seconds. Every 40 pixels it travels roots it for half a second and deals Amount damage. |
| 34 | Mirror trap | Traps | Place a trap behind the target. The first enemy crossing it receives its own most damaging basic recipe as an immediate hit. |
| 35 | Spring bed | Traps | Create a two-use spring at the caster’s tile. Each enemy triggers it once, jumping two columns right if not anchored. |
| 36 | Thorn fence crossing | Traps | Place a fence at the target column across every lane; each enemy crossing a segment takes Amount once. Lasts six seconds. |
| 37 | Burrow alarm | Traps | Mark nearby burrowing or vaulting zombies: reset their vault and stun them whenever they teleport more than one cell during six seconds. |
| 38 | Pollen filter | Traps | A stationary filter consumes one hostile projectile per second and converts its damage into nearby allied healing for five seconds. |
| 39 | Reverse mine | Traps | A trap at the target pushes enemies right only when they are moving left; stationary or retreating enemies do not trigger it. |
| 40 | Three-stage seed trap | Traps | Arm a patch for three activations: first visitor is slowed, second is silenced, third takes triple Amount and destroys the patch. |
| 41 | Watershed discharge | Ecology | Hit dry-tile enemies adjacent to water; enemies actually in water are spared. |
| 42 | Canopy shade | Ecology | For six seconds shield allies in the caster’s column only while their HP is above half; weaker allies instead get poison cleansing. |
| 43 | Roof echo | Ecology | Strike roof occupants; one second later repeat the hit only if they have stepped off that roof tile. |
| 44 | Mud bloom harvest | Ecology | Permanently dry one nearby mud tile into grass and heal all allies in that column by Amount. |
| 45 | Habitat diversity | Ecology | Hit the target once for each different terrain type occupied by nearby allied plants. |
| 46 | Thaw bank | Ecology | Convert the caster’s ice tile to grass; store its cold, then use the next cast on grass to freeze nearby enemies for two seconds. |
| 47 | Portal bud | Ecology | Move the nearest non-platform ally on a portal to the caster’s free neighboring tile; leave the portal unchanged. |
| 48 | Power-tile condenser | Ecology | Temporarily turn the caster’s boost tile to grass for six seconds and emit a triple-damage shot. Requires a boost tile. |
| 49 | Rainbow soil cycle | Ecology | Cycle the tile ahead through grass, water, roof and boost on successive casts. Existing units remain; future planting follows the new terrain. |
| 50 | Shoreline volley | Ecology | Fire a shot from every grass/water boundary in the caster’s lane; multiple boundaries create separate launch points. |
| 51 | Metronome bloom | Timing | Every third activation fires three shots; the first two activations deal no damage and bank the rhythm. |
| 52 | Damage appointment | Timing | Schedule a strike four seconds ahead. If the target is still on its original tile it takes triple Amount; otherwise normal Amount. |
| 53 | Health snapshot | Timing | Remember an ally’s current HP. Three seconds later restore at most Amount of health lost since that snapshot, without undoing death. |
| 54 | Silence window | Timing | For six seconds damage the marked enemy by Amount only when it attempts an attack while silenced. |
| 55 | After-stun second wind | Timing | Arm a six-second ward: when the caster’s stun ends, instantly reset all its other recipes once. |
| 56 | Lane afterimage | Timing | Record every enemy position in range. Two seconds later strike those locations, damaging whoever now occupies them. |
| 57 | Cooldown flower | Timing | Only while every other recipe is recharging, cut those remaining timers in half and take one second of stun. |
| 58 | Wave-bound bud | Timing | Once per wave, add Amount to maximum and current HP. Repeated casts within the same wave do nothing. |
| 59 | Collection echo | Timing | For six seconds, the first sun collected near this caster triggers one extra shot whose damage is the token value plus Amount. |
| 60 | Late bloomer | Timing | Damage grows with time since planting, but each successful shot resets the age bonus to zero. |
| 61 | Swimmer hook | Counters | Pull a swimmer to the nearest dry tile in its lane and deal Amount; fails if that lane has no dry tile. |
| 62 | Armor-seam seed | Counters | Plant a seam on an armored enemy: its next shield-absorbed hit also deals Amount pure HP damage. Single use, six seconds. |
| 63 | Rage lure | Counters | Enraged enemies are pulled toward the caster’s lane if compatible, while losing their active frenzy. |
| 64 | Healing reversal | Counters | Mark an enemy for five seconds: any increase in its HP is erased and deals Amount damage once per second. |
| 65 | Summon embargo | Counters | For six seconds new zombies entering within range arrive with every attack timer delayed by Amount/10 seconds. |
| 66 | Projectile toll booth | Counters | For six seconds the caster’s next Count intercepted enemy shots each cost their source Amount health. Shots are destroyed. |
| 67 | Shield rupture fan | Counters | Consume an enemy’s barrier and divide its remaining points as damage among other foes nearby; the shield owner takes no direct damage. |
| 68 | Hostile hazard harvest | Counters | Remove enemy-created hazard zones within range and turn each removed zone into an Amount-point shield on the caster. |
| 69 | Death-rattle mute | Counters | Suppress the nearest enemy’s configured death nova, healing, sun and split effects for six seconds. Normal death animation remains. |
| 70 | Fast-attacker tax | Counters | Hit an enemy for Amount times the number of its recipes with intervals under one second; slow attackers are unaffected. |
| 71 | Prune for power | Growth | Remove the caster’s last other recipe and permanently add half that recipe’s damage to this pruning recipe. Each cast consumes a real recipe. |
| 72 | Root-depth reserves | Growth | If the caster has stayed on the same tile since its previous cast, gain Amount shield; after three holds gain one permanent armor point. |
| 73 | Fruit budget | Growth | Spend 10% current HP, never lethal, to store one fruit. At Count+1 fruits, fire all stored health as a homing projectile. |
| 74 | Germline inheritance | Growth | Arm one inheritance: the next plant of this template gains the caster’s accumulated age as bonus shield, capped at Amount. |
| 75 | Branch points | Growth | Permanently grow one extra branch, up to Count+1. Each cast strikes that many different enemies with Amount divided equally. |
| 76 | Season rings | Growth | Cycle spring healing, summer damage, autumn sun and winter shielding on successive activations. |
| 77 | Scar bark | Growth | Convert missing HP into temporary armor for six seconds; maximum bonus is 40 percentage points. Recasting refreshes using current wounds. |
| 78 | Graft a fruit recipe | Growth | Once per caster, copy a selected allied template’s first recipe, excluding all creator expansion recipes, at half damage. |
| 79 | Height advantage | Growth | On each successful cast choose a new occupied enemy lane. Gain damage proportional to how many different lanes have been attacked. |
| 80 | Root battery | Growth | Take one second of silence and root, bank Amount energy, then release all stored energy as healing on the next cast below half health. |
| 81 | Continuous hedge | Formation | Consecutive allied plants in the caster’s row form a hedge. Give each member Amount divided by hedge length as shield. |
| 82 | Triangle focus | Formation | Requires allies above and below in the column behind. Their current HP percentages multiply a strike against the nearest enemy. |
| 83 | Rear supply line | Formation | Only allies strictly behind the caster receive healing; amount falls with column distance. |
| 84 | Alternating formation | Formation | Scan caster lane: each adjacent pair of different plant templates earns Amount/10 sun. Matching pairs earn nothing. |
| 85 | Column choir | Formation | Allies sharing the caster column each advance a different recipe index by Amount/10 seconds, cycling by row. |
| 86 | Gap-shot relay | Formation | Fire one projectile from every empty tile between the caster and the nearest forward allied plant in its row. |
| 87 | Four-corner ward | Formation | If allies occupy all four corners of a 2×2 square with this plant, cleanse only those four allies and grant Amount shield. |
| 88 | Vacant-neighbor seed | Formation | Gain Amount/4 shield for each empty orthogonal neighboring tile. A crowded plant gains nothing. |
| 89 | Frontier bloom | Formation | Only the frontmost plant in its lane can cast; it strikes once for each occupied allied column behind it. |
| 90 | Platform maintenance | Formation | Repair the supporting platform under the caster, then share any unused healing with its rider. Requires a platform. |
| 91 | Seed insurance | Recovery | Arm the caster for eight seconds: on death reset its seed recharge and grant one free copy of its packet. Once per caster. |
| 92 | Rescue lift | Recovery | Move a wounded ally one row toward the top, heal Amount, but root it for two seconds. Terrain and occupancy are checked. |
| 93 | Cleansing debt | Recovery | Remove every negative status from one ally. Delay all its recipe timers by one second per status removed. |
| 94 | Root recall | Recovery | Return the caster to its original spawn tile if available, restoring up to Amount HP lost since leaving it. |
| 95 | Mower victory voucher | Recovery | Arm the caster’s lane for eight seconds: the next mower activation grants one free caster packet instead of restoring the mower. |
| 96 | Scar transfer | Recovery | Transfer up to Amount missing HP from an ally to the caster, never reducing caster below one. Healing equals actual health paid. |
| 97 | Seed retreat | Recovery | Voluntarily remove the caster without death effects, refund half its remaining-health fraction of cost, and halve packet recharge. |
| 98 | Weather triage | Recovery | Heal an ally only while it has the weather’s matching status: snow/slow, rain/burn, storm/stun. Consume that status. |
| 99 | Borrowed bloom | Recovery | At critical HP, buy four seconds of life with Amount sun. When time runs out, return to one HP unless healed above the saved HP. |
| 100 | Last garden promise | Recovery | If this is the only living non-platform plant, gain Amount HP and reset every other recipe once. Does not repeat until another plant appears. |

## Zombie abilities

| # | Ability | Category | Mechanic |
|---|---|---|---|
| 1 | Battering sequence | Siege | Successive hits on the same plant alternate breaking its shield and striking HP. Changing targets resets to a shield-breaking blow. |
| 2 | Siege countdown | Siege | Target a plant and wait three seconds. If it survives, strike its whole column; if it dies early, caster loses half current HP. |
| 3 | Rubble barrage | Siege | Deal Amount to the nearest plant and turn its tile to blocked for two seconds only if the hit kills it. |
| 4 | Foundation breaker | Siege | Hit only platforms. If one breaks, all zombies in that lane gain a two-second frenzy. |
| 5 | Gatecrash charge | Siege | Consume an active shield to dash left by one column, then distribute the spent shield as damage to plants passed along the path. |
| 6 | Crack propagation | Siege | Hit the plant with most armor. Spread half damage to same-template plants only if the armored target survives. |
| 7 | Ransom wall | Siege | Mark a plant for four seconds. Spend up to Amount banked sun to spare it; otherwise it takes triple Amount damage. |
| 8 | Siege bridge demolition | Siege | Turn a boost tile occupied by an enemy into mud for eight seconds and drain that enemy’s shield. |
| 9 | Recipe overload | Siege | Plant targets with more than two recipes take Amount for every recipe beyond two; simple plants take no damage. |
| 10 | Demolition row | Siege | Mark the most occupied plant row. After two seconds damage occupants and briefly block only its empty tiles. |
| 11 | Sun lien | Sabotage | Mark the largest loose sun token. If collected in six seconds its full value becomes extra recharge debt on one seed packet, at one second per 25 sun. |
| 12 | Seed audit | Sabotage | Jam only packets whose templates already have two or more living plants, leaving singleton templates usable. |
| 13 | Counterfeit sunlight | Sabotage | Create an Amount-value sun token that deducts twice its value after being collected. Uncollected tokens expire normally. |
| 14 | Packet debt | Sabotage | The most expensive available packet gains Amount/10 seconds of recharge; other packets gain no debt. |
| 15 | Conveyor freezer | Sabotage | Delay the next conveyor delivery by three seconds and freeze the oldest current packet for five seconds. Conveyor only. |
| 16 | Sun shredder | Sabotage | Remove every loose sun token below Amount value; each destroyed token repairs the caster by five HP. |
| 17 | Voucher burner | Sabotage | Consume one unused free voucher or packet coupon; deal Amount damage to its corresponding plant, or the nearest plant for a voucher. |
| 18 | Sun magnet jam | Sabotage | For six seconds, loose sun close to the caster is continuously pushed away from the caster toward the board edge. |
| 19 | Price-tag strike | Sabotage | Hit the plant with highest sun cost for Amount plus one quarter of its cost; free plants are not selected. |
| 20 | Empty-bank ambush | Sabotage | Only below 25 banked sun, put the caster behind the nearest plant and take one second of stun. Does not steal sun. |
| 21 | Slipstream draft | Horde | For five seconds, the caster moves twice as fast only while another zombie is within 90 pixels directly ahead in the same lane. |
| 22 | Phalanx armor | Horde | Gain 10% damage reduction for each other zombie in the same column, capped at 50%, for six seconds. |
| 23 | Rear medic ration | Horde | Heal only zombies behind the caster; each gets more health when fewer plants remain in its lane. |
| 24 | Leader-fall orders | Horde | For eight seconds watch the frontmost other zombie. If it dies, the caster gains its remaining shield and resets all attack timers. |
| 25 | Health convoy | Horde | Move up to Amount HP from each healthier ally into the weakest zombie, stopping when it is full. No health is created. |
| 26 | Staggered march orders | Horde | Give each allied lane a half-second attack-timer advance at a different delay, top lane first. |
| 27 | Flank pack | Horde | If zombies occupy both neighboring lanes, strike the nearest plant from all three lanes for Amount each. |
| 28 | Rank swap | Horde | Exchange the frontmost and rearmost zombies in the caster lane; each trades its current shield points with the other. |
| 29 | Banner quota | Horde | If at least Count+1 different zombie templates are nearby, grant all a brief frenzy; otherwise shield only the caster. |
| 30 | Body screen | Horde | For six seconds, friendly zombies directly behind the caster take half projectile damage while the caster remains alive. |
| 31 | Acquired taste | Predation | Remember the first bitten plant template; later bites against that template heal the zombie for Amount/2. Different templates reset the memory. |
| 32 | Stored bite | Predation | Deal half Amount now and record it. The next cast on the same target releases all recorded bite damage; switching target loses the stored bite. |
| 33 | Leaf-count appetite | Predation | Hit for Amount plus five per active status or active shield/buff currently on the target. |
| 34 | Digestive pause | Predation | Consume the caster’s active shield as healing, then silence and root itself for two seconds. Does not create extra HP. |
| 35 | Second serving | Predation | Hit a target; if it dies, immediately hit the next plant farther left in the same lane for double Amount. |
| 36 | Sap drink | Predation | Steal regeneration for six seconds: regenerative plants lose that trait temporarily while caster heals five HP per second. |
| 37 | Hunger gauge | Predation | Each cast with no plant within 100 pixels stores one hunger. The next close bite spends all hunger as 25% extra damage per stack. |
| 38 | Tough chew | Predation | Bite for Amount. If armor prevents at least half the hit, instead add Amount shield to the caster. |
| 39 | Sprout meal | Predation | Target the youngest plant; damage falls as the plant ages, with full Amount against freshly planted sprouts. |
| 40 | Last-bite promise | Predation | Arm for six seconds: the next close attack on a plant below 15% HP finishes it and permanently adds Amount maximum HP to the caster. |
| 41 | Recipe blind spot | Terror | Disable only the target’s highest-damage recipe for five seconds; other recipes keep working. |
| 42 | Root panic | Terror | For five seconds, damage this plant by Amount whenever it changes tiles. Anchored stationary plants avoid the penalty. |
| 43 | Echo dread | Terror | Mark a plant’s recipe type. Its next second consecutive use of that type stuns it for two seconds; six-second window. |
| 44 | Lonely curse | Terror | For six seconds, marked plant loses Amount HP per second only while no other plant is within 120 pixels. |
| 45 | Crowded curse | Terror | Force adjacent plants to share a four-second silence if at least three occupy neighboring tiles around the target. |
| 46 | Packet fear | Terror | For six seconds the first newly planted copy of the target template arrives stunned for two seconds, then clears the curse. |
| 47 | Slow clock | Terror | For five seconds the target’s recharge rate slows in proportion to how many other recipes it has, capped at one fifth speed. |
| 48 | Fake opening | Terror | For six seconds the caster’s first received hit makes it immune for half a second and roots the attacking plant for two seconds. |
| 49 | Sun dread | Terror | For six seconds each sun collected stuns this marked plant for a quarter second. Collection still grants normal sun. |
| 50 | Overgrowth knot | Terror | Turn the target plant’s movement speed into self-damage over three seconds while rooting it. Stationary plants take no damage. |
| 51 | Sidewalk runner | Mobility | Move to the least occupied compatible adjacent lane, but only if that lane has fewer plants than the current lane. |
| 52 | Tile-edge hopper | Mobility | Jump left one tile only if the destination terrain differs from the current terrain; otherwise gain Amount shield. |
| 53 | Formation leap | Mobility | Jump over an entire contiguous group of friendly zombies, landing just left of its frontmost member. |
| 54 | Reverse gear | Mobility | Retreat right by one column and leave a one-second silence on every plant at the abandoned column. |
| 55 | Pincer rendezvous | Mobility | Move to the lane of the allied zombie farthest left, but land one tile behind it. Cannot move closer to the house than that ally. |
| 56 | Tunnel exit marker | Mobility | First cast records a position. Next cast returns there and deals Amount to plants around that original exit. |
| 57 | Wind sail | Mobility | During wind, move left Amount pixels; during rain, move to a compatible lane above; during other weather do nothing. |
| 58 | Charged lane crossing | Mobility | Take half a second of stun, then jump into the most populated compatible plant lane and gain Amount shield. |
| 59 | Rubber-band pursuit | Mobility | Attach to a plant for five seconds: if separation grows above 200 pixels, snap to 90 pixels to its right once. |
| 60 | Mower sidestep | Mobility | When an active mower approaches within 180 pixels, flee to a compatible adjacent lane. Does not restore or remove the mower. |
| 61 | Grave cache | Remains | Consume one unused fallen zombie record to shield the caster by that template’s armor times Amount plus ten. |
| 62 | Grave bomb | Remains | Consume a fallen zombie record; after two seconds explode at its recorded tile rather than reviving it. |
| 63 | Recipe wake | Remains | Consume a fallen zombie record and fire its first basic recipe once from the caster. No zombie is revived. |
| 64 | Remnant armor | Remains | For six seconds, each nearby allied death grants the caster Amount shield, capped at Count triggers. |
| 65 | Replacement ticket | Remains | Arm a one-time ticket: when the caster dies, spawn the selected zombie template at the right edge in the same lane after three seconds. |
| 66 | Grave tax | Remains | Consume up to Count fallen plant records; each removes Amount/10 sun from the bank. Cannot reuse records. |
| 67 | Delayed twins | Remains | Spawn the selected template in top and bottom compatible lanes after different delays. Each child starts at half health. |
| 68 | Vacant-lane delivery | Remains | Summon selected zombie template only in compatible lanes currently containing no zombies; Count caps new arrivals. |
| 69 | Corpse compass | Remains | Move into the lane of the most recent fallen plant and heal Amount; its fallen record is consumed. |
| 70 | Inherited bite | Remains | Consume a fallen zombie record and permanently add one tenth its maximum health to caster’s first melee recipe, capped at Amount. |
| 71 | Backfire barrel | Weapons | Catch the nearest hostile shot, destroy it, and fire two weaker shots backward and forward with its damage divided equally. |
| 72 | Crosswind shrapnel | Weapons | Fire into every lane, with shots starting at the caster’s column but traveling left; outer lanes get less damage. |
| 73 | Packet hunter missile | Weapons | Hit the plant whose packet has the longest current recharge; missing or unused packet plants are ignored. |
| 74 | Ricochet debt | Weapons | Tag a plant: the next projectile damage it receives delays a different allied plant’s attack timers by Amount/10 seconds. |
| 75 | Ammo scavenger | Weapons | Destroy up to Count friendly projectiles and bank their damage. Next activation with no friendly shots releases the bank as one direct hit. |
| 76 | Cover fire corridor | Weapons | For five seconds, destroy hostile projectiles only in the strip between the caster and its nearest ally in the same lane. |
| 77 | Roof drill | Weapons | Damage roof plants and reduce their armor by five percentage points. Non-roof plants are not selected. |
| 78 | Skip-shot targeting | Weapons | Strike every second plant in the lane ordered from right to left, skipping the frontmost blocker. |
| 79 | Dead-angle strike | Weapons | Damage plants farther than one column from any other plant, but only if they have an offensive basic recipe. |
| 80 | Shot mortgage | Weapons | Delay the caster’s next attack by three seconds to fire Count projectiles immediately from progressively farther-left columns. |
| 81 | Storm debt | Weathercraft | In a storm, hit a nearby plant for Amount, grant caster weather immunity for three seconds and set the next storm strike three seconds away. |
| 82 | Frost-bite thaw | Weathercraft | During snow, consume a slowed plant’s slow effect to steal Amount HP; outside snow do nothing. |
| 83 | Fog loan | Weathercraft | During fog, halve caster HP, never lethal, to gain a shield worth twice HP sacrificed. Once per fog period. |
| 84 | Heat sink | Weathercraft | In heat, consume nearby burning allied zombies’ burn to advance caster timers by one second per cured ally. |
| 85 | Rain rust | Weathercraft | In rain, reduce shields on every nearby plant by Amount each second for three seconds. Does not directly damage HP. |
| 86 | Mud wake | Weathercraft | Leave three mud tiles behind the walking zombie, each restoring after five seconds. The current tile is unchanged. |
| 87 | Pool siphon | Weathercraft | Turn one occupied water tile to grass for six seconds; any plant on that tile loses Amount shield and is silenced for one second. |
| 88 | Portal sickness | Weathercraft | A six-second curse on the target: whenever it occupies a portal tile, its HP is drained by Amount per second. |
| 89 | Boost hijack | Weathercraft | While on a power tile, the caster heals Amount and changes that tile to roof for four seconds. |
| 90 | Leaf-storm camouflage | Weathercraft | During falling leaves, all nearby zombies become immune for half a second; the caster then takes Amount self-damage. |
| 91 | Outnumbered odds | Adaptation | When plants outnumber zombies in range, hit the target for Amount times that count difference, capped at five. |
| 92 | Wounded sprint budget | Adaptation | Convert missing HP into leftward movement, up to Amount pixels, then heal exactly one HP. No movement at full health. |
| 93 | Armor diet | Adaptation | Shed up to ten percentage points of caster armor and gain four times Amount shield; cannot use at zero armor. |
| 94 | Target memory | Adaptation | Each time a different plant template is attacked, bank one stack; revisiting a remembered template spends all stacks as extra Amount damage. |
| 95 | Wave debt collector | Adaptation | Once each wave, remove up to Amount sun. Every ten sun actually removed heals caster one HP. |
| 96 | Two-faced armor | Adaptation | Alternate between resisting melee by 70% and resisting ranged basic attacks by 70% for four seconds per cast. |
| 97 | Shield deadline | Adaptation | Receive Amount shield for three seconds. If any remains at expiry, turn it into a hit against the nearest plant; otherwise stun the caster. |
| 98 | Power scent | Adaptation | Prioritize the plant with most current shield plus buffed health. If neither exists, do not attack. |
| 99 | Twin thresholds | Adaptation | Above 75% HP hit a plant; below 25% heal self; in between, sacrifice Amount/2 HP to shield the weakest ally for Amount. |
| 100 | Final order | Adaptation | If the caster is the last zombie in its lane, arm a death strike against the healthiest plant in that lane. Otherwise remove the armed order. |
