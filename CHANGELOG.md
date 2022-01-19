# Changelog

<!--next-version-placeholder-->

## v3.3.0 (2021-07-09)
### Feature
* "feral" lore for non-taimed pet hats ([`d163307`](https://github.com/OrangeUtan/Hats/commit/d163307e5f5cac74833115948114b7b509d952dd))
* Owners name as lore on pet hats ([`e2b0bd9`](https://github.com/OrangeUtan/Hats/commit/e2b0bd9354ff44311d98e34fa23e58b1a1a6b6e1))
* Tamed cats can be converted to hats ([`87afca6`](https://github.com/OrangeUtan/Hats/commit/87afca64946f1b3b48e6f0f96b3e4375dcf7c674))

### Fix
* Feral pet hats summon named mobs ([`32b94dd`](https://github.com/OrangeUtan/Hats/commit/32b94dd21ea848911ab093946fc602b5aea4c57a))
* Feral pet hats now spawn feral mobs ([`5aa82b0`](https://github.com/OrangeUtan/Hats/commit/5aa82b0d7d5209654fe80a3884d06ee027dc6829))
* Rename setting dog_conversion to pet_conversion ([`8639037`](https://github.com/OrangeUtan/Hats/commit/8639037e6d7cfac1649c7b9f6e171f3b045fb07b))
* Settings not working when updating datapack ([`1aab603`](https://github.com/OrangeUtan/Hats/commit/1aab603b21997b043f46820afa7191d5c9efeff4))

### Balancing
* Librarian trades 3D glasses ([`aa53cec`](https://github.com/OrangeUtan/Hats/commit/aa53cec74a4be3bc440919fb4e07642ce7e01356))

### Performance
* Remove duplicate check for pets ([`eecdd51`](https://github.com/OrangeUtan/Hats/commit/eecdd51982bd3cdd8f07e355f19b32a6258f90e6))

## v3.2.1 (2021-07-08)
### Balancing
* Remove feather_headband_recipe ([`ec2fcec`](https://github.com/OrangeUtan/Hats/commit/ec2fcec361dbd6e595e666f6a624142e660a3d85))
* Remove recipes for glasses ([`b3eace8`](https://github.com/OrangeUtan/Hats/commit/b3eace830caab5913a8500f9309da91245683037))

## v3.2.0 (2021-07-07)
### Feature
* Head hats no longer stackable ([`6da3341`](https://github.com/OrangeUtan/Hats/commit/6da3341b43c10d55c0ed2dec1a7a1262e763d801))

### Documentation
* Update function docs ([`ffbc76a`](https://github.com/OrangeUtan/Hats/commit/ffbc76a4010532d082c23d39a55c1277e310fbea))

## v3.1.0 (2021-07-06)
### Feature
* Chat configuration ([`2612506`](https://github.com/OrangeUtan/Hats/commit/2612506b9688817a0701976f8d2c7788a9a894c8))

## v3.0.0 (2021-07-03)
### Feature
* Recipes for all glasses ([`483fc20`](https://github.com/OrangeUtan/Hats/commit/483fc20f562716a3a571c70b0aba23c515836bf4))
* Recipe for Feather Headband ([`ce72523`](https://github.com/OrangeUtan/Hats/commit/ce725232c401262589dadfabcd5e15bddc8562e9))
* Crafting recipes for toad hats ([`985b33c`](https://github.com/OrangeUtan/Hats/commit/985b33cbcafd033d705a22a6025f5bbda3fcd93e))
* Hat loot tables no longer grouped by category ([`bd2831f`](https://github.com/OrangeUtan/Hats/commit/bd2831fa68a5ff96957e9ed6f3d3f7b7660a9c74))
* Datapack advancement ([`c4ef51d`](https://github.com/OrangeUtan/Hats/commit/c4ef51d4c4324856bbefab60109871e47d2056e5))

### Fix
* Load function not executed ([`dc2fc3a`](https://github.com/OrangeUtan/Hats/commit/dc2fc3a11dbb2db702844901c03941ec886f7938))
* Yellow shulker box method not working ([`0b07bfd`](https://github.com/OrangeUtan/Hats/commit/0b07bfd244539148496eaf3a44c92e09aac99fc3))
* Renamed "native_american_headband" to "feather headband" ([`3d06f2e`](https://github.com/OrangeUtan/Hats/commit/3d06f2e3ddab081734be432f1bd4918d03374ab9))
* Resourcepack didn't display hats if built from cache ([`1e74309`](https://github.com/OrangeUtan/Hats/commit/1e74309d15f6fa290b3c3903c924c1e93d893007))
* Changed 3D glasses type to "three_d_glass" ([`bedf278`](https://github.com/OrangeUtan/Hats/commit/bedf278d59cfde30acb40b8dc04722bd01fbfedf))
* Rainbow glasses was not displayed ([`47c8ffa`](https://github.com/OrangeUtan/Hats/commit/47c8ffa1d0c44577f9d1da7573b73fc6fd2b4644))

### Breaking
* Changed datapack namespace ([`e86e110`](https://github.com/OrangeUtan/Hats/commit/e86e1108d50b0c871119a0076e85aefb60612327))
* Changed all hat CustomModelData ([` 5e899ae`](https://github.com/OrangeUtan/Hats/commit/5e899aedc9ab2dee830fccacf580934b96fb0c8a))
* Changed types of hats:
  * Squid to posh_squid  ([`1bcf7c9`](https://github.com/OrangeUtan/Hats/commit/1bcf7c960953f45434b8d94c7459d84d2dcdb448))
  * Flattened hat types ([`2ba0bba`](https://github.com/OrangeUtan/Hats/commit/2ba0bba255d6f4e9ad0e3914c4b3a984e24b84c3))

## [2.3.1] - 2020-06-17
### Added
- Configuration book
#### Hats
- `dog`
- `earth`

### Internal
#### Added
- Install function
- Ability to add custom loot to chests
#### Changed
- Using mcanitexgen to generate texture animations
- Advancements now query for hat type NBT tag instead of Custom Model Data
#### Removed
- Removed **is_hat** tag from all hats

## [2.3.0] - 2020-05-27
### Added
- Villager profession trades
- Wandering Trader now can have a favorite cat
- German translation
- Added some lore to hats
- Removing storage and advancements on uninstall

### Changed
- Villagers favorite cats are now dependent on biome
- Zombies only get dressed with Jason Mask at around midnight
- Wiggly Ghasts can only be found in mansions at night
#### Performance
- Only mobs near player get dressed
- Scheduling functions in different intervals instead of using **tick.mcfunction**
- Using shulkerbox method for hat mechanic
- Using advancements to trigger hat mechanic
- Replaced some NBT selectors

### Removed
- **fix_hat/...** functions. Replaced with shulkerbox method

### Fixed
- Villagers were dressed with wrong hat item

### Internal
#### Added
- Central hat registry for code generation
#### Changed
- Using predicates for randomnes and checks
- Using loot tables for random trade prices
- Generating item models for hats
- Generating hat loot tables
- Generating **_all** and **_rand** category loot tables

## [2.2.1] - 2020-05-17

### Internal
#### Added
- Github Action to create releases
#### Changed
- Combined hats resourcepack and datapack into one repository

## [2.2.0] - 2019-10-29
### Added
- `Wiggly Ghast` hat
- `Native American Headband` hat
- `Jason Mask`
- Dressing Zombie Pigmans
- Zombies can be dressed with Jason Mask
- Loot tables for all hats

### Removed
- **/equip** and **/give** functions. Use loot tables instead
- Removed **give_all_...** function tags

### Fixed
- `Arrow` and `Red Snorkel Mask` were not displaying on players head

### Internal
#### Added
- Added Item tags for the items used as hats
- Added **is_hat**, **hats.hat** and hat type NBT tags to all hats. Gives more information than just the Custom Model Data
- Added **_all** and **_rand** loot tables for each categories
#### Changed
- Using loot tables instead of functions for hat behaviour (equip, give, etc.)
- Using the new hat loot tables for dressing and trades
- Using **hats.mob.dont_dress** instead of **hats_is_dressed** tag to indicate mob is already dressed

## [2.1.0] - 2019-10-10
### Added
- Special trades for armorer, librarian and toolsmith villagers
- Dressing Wandering Trader
- Function tags to receive all hats for each category
#### Hats
- `Frying pan`
- `Luigi` and `Mario`
- `Mario Cap`, `Luigi Cap` and `Cappy`
- `Toad Blue`, `Toad Green`, `Toad Red` and `Toad Yellow`
- `Armorer`
- `Farmer`
- `Villager Nose`
- `Tophat with Monocle`

### Changed
- Renamed hat **glasses/3D** to **glasses/three_d**

### Internal
- Using loot tables instead of functions to dress mobs
