from services.auxiliar import dict_by_id
from models import ( 
    FM_dead_ball_stats, FM_goalkeeper_stats, FM_mental_stats, FM_physical_stats, FM_technical_stats,
    Player_performance, Duel_performance, Passing_performance, Shooting_performance, Goalkeeping_performance, 
    Possession_performance, Defensive_performance, Shots_goals_creation_performance
)

def get_player_fm24_data(db, player_id):
    mental_stats = db.query(FM_mental_stats).filter(FM_mental_stats.player_id == player_id).all()
    physical_stats = db.query(FM_physical_stats).filter(FM_physical_stats.player_id == player_id).all()
    technical_stats = db.query(FM_technical_stats).filter(FM_technical_stats.player_id == player_id).all()
    dead_ball_stats = db.query(FM_dead_ball_stats).filter(FM_dead_ball_stats.player_id == player_id).all()
    goalkeeper_stats = db.query(FM_goalkeeper_stats).filter(FM_goalkeeper_stats.player_id == player_id).all()

    fm24_data = {
        "physical_stats": dict_by_id(physical_stats, "player_id", player_id),
        "technical_stats": dict_by_id(technical_stats, "player_id", player_id),
        "dead_ball_stats": dict_by_id(dead_ball_stats, "player_id", player_id),
        "mental_stats": dict_by_id(mental_stats, "player_id", player_id),
        "goalkeeper_stats": dict_by_id(goalkeeper_stats, "player_id", player_id),
    }

    return fm24_data

def get_player_performance(db, player_id):
    performance = db.query(Player_performance).filter(Player_performance.player_id == player_id).first()
    if not performance:
        return None

    performances_id = performance.performance_id

    duel_stats = db.query(Duel_performance).filter(Duel_performance.performance_id == performances_id).all()
    passing_stats = db.query(Passing_performance).filter(Passing_performance.performance_id == performances_id).all()
    shooting_stats = db.query(Shooting_performance).filter(Shooting_performance.performance_id == performances_id).all()
    goalkeeping_stats_perf = db.query(Goalkeeping_performance).filter(Goalkeeping_performance.performance_id == performances_id).all()
    possession_stats = db.query(Possession_performance).filter(Possession_performance.performance_id == performances_id).all()
    defensive_stats = db.query(Defensive_performance).filter(Defensive_performance.performance_id == performances_id).all()
    shots_goals_creation_stats = db.query(Shots_goals_creation_performance).filter(Shots_goals_creation_performance.performance_id == performances_id).all()

    performances_data = {
        "shooting_stats": dict_by_id(shooting_stats, "performance_id", performances_id),
        "possession_stats": dict_by_id(possession_stats, "performance_id", performances_id),
        "passing_stats": dict_by_id(passing_stats, "performance_id", performances_id),
        "duel_stats": dict_by_id(duel_stats, "performance_id", performances_id),
        "shots_goals_creation_stats": dict_by_id(shots_goals_creation_stats, "performance_id", performances_id),
        "defensive_stats": dict_by_id(defensive_stats, "performance_id", performances_id),
        "goalkeeping_stats": dict_by_id(goalkeeping_stats_perf, "performance_id", performances_id),
    }

    return performances_data