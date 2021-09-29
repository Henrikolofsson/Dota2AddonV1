local Game_states = {}

---@return boolean
function Game_states:Is_hero_selection_state()
    return GameRules:State_Get() == DOTA_GAMERULES_STATE_HERO_SELECTION
end

---@return boolean
function Game_states:Is_pre_game_state()
    return GameRules:State_Get() == DOTA_GAMERULES_STATE_PRE_GAME
end

---@return boolean
function Game_states:Is_game_in_progress_state()
    return GameRules:State_Get() == DOTA_GAMERULES_STATE_GAME_IN_PROGRESS
end

return Game_states