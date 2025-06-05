import pygame
from scripts.structure.assets import *
from scripts.projectiles.projectile import e_Projectile
import random
import math

#enemies ship sprite class definition,
# enemie ship 1 and 2 and bosses

class EnemiesShip(pygame.sprite.DirtySprite):
    def __init__(self, size, position, speed, score, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos: tuple = position
        self.size: tuple = size
        self.speed: int = speed
        self.score: int = score
        self.image: pygame.Surface = pygame.transform.scale(EnemiesShipsAssets().e_ships_1,
                                            self.size)  # bad ship size
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)

        # explosion control
        self.alive_state: bool = True
        self.exploded_time: int = 0
        # life control
        self.lives: int = 3
        # projectile control
        self.projectile_state: bool = False
        self.last_projectile: int = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def explode(self):
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_exploded_1,
                                            (110, 80))  # bad ship size
        self.rect.x -= 30
        self.rect.y -= 10
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False


class EnemiesShip2(pygame.sprite.DirtySprite):
    def __init__(self, size, position, speed, score, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)

        self.pos = position
        self.size = size
        self.speed: int = speed
        self.score: int = score
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_2,
                                            self.size)  # bad ship size
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)

        # explosion control
        self.alive_state = True
        self.exploded_time = 0
        # life control
        self.lives = 2
        # projectile control
        self.projectile_state = True
        self.last_projectile = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def explode(self):
        self.image = pygame.transform.scale(EnemiesShipsAssets().e_ships_exploded_1,
                                            (110, 80))  # bad ship size
        self.rect.x -= 30
        self.rect.y -= 10
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False



class Boss(pygame.sprite.DirtySprite):
    def __init__(self, position, size, health, score, projectile_groups, *groups):
        pygame.sprite.DirtySprite.__init__(self, *groups)
        
        # Basic properties
        self.pos = position
        self.size = size
        self.max_health = health
        self.health = self.max_health
        self.score = score
        self.projectile_groups = projectile_groups  # Group to add projectiles to
        
        # Load boss image (you'll need to create/update this in EnemiesShipsAssets)
        self.image = pygame.transform.scale(BossesAssets().bosses_image_1, self.size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        
        # Movement variables
        self.base_speed = 3
        self.speed = self.base_speed
        self.movement_pattern = "entrance"
        self.pattern_start_time = pygame.time.get_ticks()
        self.direction = 1  # 1 for right, -1 for left
        self.target_position = None
        self.pattern_duration = 10000  # Time before changing patterns (ms)
        
        # Attack variables
        self.last_attack_time = 0
        self.attack_cooldown = 800  # ms between attacks
        self.attack_pattern = "single"
        self.bullet_speed = 7
        self.dodge_cooldown = 0
        self.dodge_threshold = 150  # Distance to consider dodging player projectiles
        
        # Phase transition
        self.phase = 1
        self.max_phases = 3
        self.phase_health_threshold = self.max_health / self.max_phases
        
        # State tracking
        self.alive_state = True
        self.exploded_time = 0
        self.invulnerable = False
        self.invulnerable_time = 0
        self.invulnerable_duration = 1500  # ms of invulnerability after phase change
        
        # Animation variables
        self.flash_timer = 0
        self.is_flashing = False

    def update(self, player_position, player_projectiles, time_elapsed):
        if not self.alive_state:
            return
            
        # Check for phase transitions
        self.check_phase_transition()
        
        # Handle invulnerability
        if self.invulnerable and pygame.time.get_ticks() - self.invulnerable_time > self.invulnerable_duration:
            self.invulnerable = False
            
        # Update flashing animation
        if self.is_flashing:
            self.flash_timer -= time_elapsed
            if self.flash_timer <= 0:
                self.is_flashing = False
                self.image = pygame.transform.scale(BossesAssets().bosses_image1, self.size)
        
        # Movement based on current pattern
        self.move_pattern(time_elapsed)
        
        # Dodge player projectiles if not in special movement patterns
        if self.movement_pattern not in ["entrance", "phase_transition"] and self.dodge_cooldown <= 0:
            self.try_dodge_projectiles(player_projectiles, time_elapsed)
        else:
            self.dodge_cooldown -= time_elapsed
            
        # Attack player
        if pygame.time.get_ticks() - self.last_attack_time > self.attack_cooldown:
            self.attack(player_position)
            
        # Check if it's time to change patterns
        current_time = pygame.time.get_ticks()
        if current_time - self.pattern_start_time > self.pattern_duration and self.movement_pattern not in ["entrance", "phase_transition"]:
            self.change_pattern()

    def move_pattern(self, time_elapsed):
        """Execute the current movement pattern"""
        delta_speed = self.speed * (time_elapsed / 1000)
        
        if self.movement_pattern == "entrance":
            # Boss flies in from top of screen
            if self.rect.y < 100:
                self.rect.y += delta_speed * 2
            else:
                self.movement_pattern = "side_to_side"
                self.pattern_start_time = pygame.time.get_ticks()
                
        elif self.movement_pattern == "side_to_side":
            # Move horizontally back and forth
            self.rect.x += self.direction * delta_speed * 3
            
            # Reverse direction at screen edges (with padding)
            screen_width = pygame.display.get_surface().get_width()
            if self.rect.right > screen_width - 50:
                self.direction = -1
            elif self.rect.left < 50:
                self.direction = 1
                
        elif self.movement_pattern == "circle":
            # Move in a circular pattern
            center_x = pygame.display.get_surface().get_width() // 2
            center_y = 200
            radius = 150
            angle = (pygame.time.get_ticks() - self.pattern_start_time) / 1000 * self.speed
            
            self.rect.x = center_x + math.cos(angle) * radius - self.rect.width // 2
            self.rect.y = center_y + math.sin(angle) * radius - self.rect.height // 2
            
        elif self.movement_pattern == "charge":
            # If no target position, pick one
            if not self.target_position:
                screen_width = pygame.display.get_surface().get_width()
                screen_height = pygame.display.get_surface().get_height()
                self.target_position = (random.randint(50, screen_width-50), random.randint(50, 250))
                
            # Move toward target position
            dx = self.target_position[0] - self.rect.centerx
            dy = self.target_position[1] - self.rect.centery
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance > delta_speed * 5:
                self.rect.x += dx / distance * delta_speed * 5
                self.rect.y += dy / distance * delta_speed * 5
            else:
                self.target_position = None
                
        elif self.movement_pattern == "phase_transition":
            # Move to center and flash
            center_x = pygame.display.get_surface().get_width() // 2 - self.rect.width // 2
            center_y = 150
            
            dx = center_x - self.rect.x
            dy = center_y - self.rect.y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance > delta_speed:
                self.rect.x += dx / distance * delta_speed
                self.rect.y += dy / distance * delta_speed
            else:
                # Once centered, switch back to a regular pattern
                self.movement_pattern = random.choice(["side_to_side", "circle", "charge"])
                self.pattern_start_time = pygame.time.get_ticks()

    def change_pattern(self):
        """Change to a new movement pattern"""
        patterns = ["side_to_side", "circle", "charge"]
        # Don't pick the same pattern twice in a row
        available_patterns = [p for p in patterns if p != self.movement_pattern]
        self.movement_pattern = random.choice(available_patterns)
        self.pattern_start_time = pygame.time.get_ticks()
        
        # Reset pattern-specific variables
        if self.movement_pattern == "charge":
            self.target_position = None
        elif self.movement_pattern == "side_to_side":
            self.direction = random.choice([-1, 1])
            
        # Also change attack pattern sometimes
        if random.random() < 0.5:
            attack_patterns = ["single", "spread", "burst"]
            self.attack_pattern = random.choice(attack_patterns)

    def attack(self, player_position):
        """Generate projectiles based on current attack pattern"""
          # Import here to avoid circular imports
        
        self.last_attack_time = pygame.time.get_ticks()
        
        if self.attack_pattern == "single":
            # Single direct shot at player
            self._fire_at_target(player_position)
            
        elif self.attack_pattern == "spread":
            # Fire multiple projectiles in a spread
            for angle_offset in [-20, -10, 0, 10, 20]:
                angle = self._calculate_angle_to_target(player_position) + angle_offset
                dx = math.cos(math.radians(angle)) * self.bullet_speed
                dy = math.sin(math.radians(angle)) * self.bullet_speed
                
                projectile = e_Projectile(
                    (self.rect.centerx, self.rect.bottom),
                    (20, 20),  # Size
                    (dx, dy),  # Velocity
                    self.projectile_groups
                )
                
        elif self.attack_pattern == "burst":
            # Quick burst of 3 shots
            self._fire_at_target(player_position)
            
            # Schedule additional shots
            pygame.time.set_timer(pygame.USEREVENT + 1, 150, 2)  # Fire 2 more times at 150ms intervals

    def _fire_at_target(self, target_position):
        """Fire a projectile toward target position"""

        
        angle = self._calculate_angle_to_target(target_position)
        dx = math.cos(math.radians(angle)) * self.bullet_speed
        dy = math.sin(math.radians(angle)) * self.bullet_speed
        
        projectile = e_Projectile(
            (self.rect.centerx, self.rect.bottom),
            (20, 20),  # Size
            (dx, dy),  # Velocity
            self.projectile_groups
        )
    
    def _calculate_angle_to_target(self, target_position):
        """Calculate angle in degrees to target"""
        dx = target_position[0] - self.rect.centerx
        dy = target_position[1] - self.rect.centery
        angle = math.degrees(math.atan2(dy, dx))
        return angle
    
    def try_dodge_projectiles(self, player_projectiles, time_elapsed):
        """Try to dodge incoming player projectiles"""
        delta_speed = self.speed * (time_elapsed / 1000) * 1.5  # Faster dodge speed
        
        for projectile in player_projectiles:
            # Check if projectile is heading toward the boss
            if (self.rect.left < projectile.rect.centerx < self.rect.right and
                projectile.rect.centery < self.rect.centery and
                self.rect.centery - projectile.rect.centery < self.dodge_threshold):
                
                # Determine which way to dodge (left or right)
                screen_width = pygame.display.get_surface().get_width()
                if self.rect.centerx < screen_width / 2:
                    # Move right if on left side
                    self.rect.x += delta_speed * 10
                else:
                    # Move left if on right side
                    self.rect.x -= delta_speed * 10
                    
                self.dodge_cooldown = 500  # Cooldown before next dodge
                return
    
    def take_damage(self, damage=1):
        """Handle boss taking damage"""
        if not self.alive_state or self.invulnerable:
            return
            
        self.health -= damage
        
        # Visual feedback for damage
        self.is_flashing = True
        self.flash_timer = 100  # Flash for 100ms
        self.image = pygame.transform.scale(BossesAssets().bosses_damaged_image1, self.size)
        
        # Check if dead
        if self.health <= 0:
            self.explode()
            return
            
        # Check for phase transition
        self.check_phase_transition()
    
    def check_phase_transition(self):
        """Check if boss should transition to next phase"""
        current_phase_threshold = self.max_health - (self.phase * self.phase_health_threshold)
        
        if self.health <= current_phase_threshold and self.phase < self.max_phases:
            self.transition_to_next_phase()
    
    def transition_to_next_phase(self):
        """Transition to next phase with new behavior"""
        self.phase += 1
        
        # Make invulnerable during transition
        self.invulnerable = True
        self.invulnerable_time = pygame.time.get_ticks()
        
        # Change movement pattern
        self.movement_pattern = "phase_transition"
        self.pattern_start_time = pygame.time.get_ticks()
        
        # Increase difficulty with each phase
        self.speed = self.base_speed + (self.phase - 1) * 0.5
        self.attack_cooldown = max(300, self.attack_cooldown - 200)  # Faster attacks, minimum 300ms
        
        # Visual feedback
        self.is_flashing = True
        self.flash_timer = 500  # Longer flash for phase transition
        
        # Each phase has unique attack patterns
        if self.phase == 2:
            self.attack_pattern = "spread"
        elif self.phase == 3:
            self.attack_pattern = "burst"
    
    def explode(self):
        """Handle boss explosion"""
        self.image = pygame.transform.scale(BossesAssets().bosses_exploded_image1, 
                                           (self.size[0] * 1.5, self.size[1] * 1.5))
        self.rect.x -= self.size[0] * 0.25
        self.rect.y -= self.size[0] * 0.25
        self.exploded_time = pygame.time.get_ticks()
        self.alive_state = False
