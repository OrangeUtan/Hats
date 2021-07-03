# Changelog

<!--next-version-placeholder-->

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
