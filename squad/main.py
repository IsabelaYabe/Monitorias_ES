from visitor import Archer, Cavalry, Spearman, AttackAction, MoveAction, SpecialAttackAction, UnitGroup
from state import Level1

if __name__ == "__main__":
    archer = Archer("Green Archer", Level1())
    cavalry = Cavalry("Red Cavalry", Level1())
    spearman = Spearman("Blue Spearman", Level1())

    squad = UnitGroup("Squad Alpha", Level1())
    squad.add(archer)
    squad.add(cavalry)
    squad.add(spearman)

    normal_attack = AttackAction()
    move_action = MoveAction()
    special_attack = SpecialAttackAction()

    print("--- Ataque individual ---")
    archer.accept(normal_attack)

    print("\n--- Ataque do grupo ---")
    squad.accept(normal_attack)

    print("\n--- Especial do grupo (Level 1) ---")
    squad.accept(special_attack)

    print("\n--- Grupo subiu de nível ---")
    squad.level_up()          # agora Level2
    squad.accept(special_attack)

    print("\n--- Grupo subiu de nível de novo ---")
    squad.level_up()          # agora Level3 (MAX)
    squad.accept(special_attack)

    print("\n--- Movimento do grupo ---")
    squad.accept(move_action)

    print("\n--- Tentando subir de nível além do máximo ---")
    squad.level_up()          # já está no máximo