from manim import *

TITLE_COLOR = "#91caed"

class AutomataDiagram(Scene):
    def construct(self):
        self.theory_of_computation()
        current_rect, group = self.comb_logic()
        group = self.fsm(group)
        group = self.pushdown(group)
        group = self.turing(group)

        self.wait()
        group = self.highlight(current_rect, group)
        self.wait()

    def theory_of_computation(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)
        toc = Text("Theory of Computation", font="Oxygen Bold", color=TITLE_COLOR)
        self.play(Write(toc))
        self.play(toc.animate.shift(UP * 3))
        self.play(Write(Underline(toc)))

    def comb_logic(self):
        comb = Text("Combinatorial Logic", font="Oxygen")
        comb_rect = RoundedRectangle(corner_radius=0.5, width=7)
        self.play(Create(comb_rect), Write(comb))

        comb_box = Group(comb_rect, comb)
        self.play(comb_box.animate.scale(0.7).shift(RIGHT * 0.5 + DOWN))

        return comb_rect, comb_box

    def fsm(self, group):
        fsm = Text("Finite State Machines", font="Oxygen").shift(UP * 0.5 + LEFT * 0.5).scale(0.7)
        fsm_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3).shift(DOWN * 0.5)
        self.play(Write(fsm), Create(fsm_rect))

        box = Group(group, fsm, fsm_rect)
        self.play(box.animate.scale(0.75).shift(RIGHT * 0.46 + DOWN * 0.75))

        return box

    def pushdown(self, group):
        pushd = Text("Pushdown Automata", font="Oxygen").shift(UP * 0.3 + LEFT * 1.1).scale(0.7 * 0.75)
        pushd_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3.3).shift(DOWN)
        self.play(Write(pushd), Create(pushd_rect))

        box = Group(group, pushd, pushd_rect)
        self.play(box.animate.scale(0.75).shift(RIGHT * 0.6, DOWN * 0.2))

        return box

    def turing(self, group):
        turing = Text("Turing Machines", font="Oxygen").shift(UP * 0.305 + LEFT * 1.8).scale(0.7 * 0.75 * 0.75)
        turing_rect = RoundedRectangle(corner_radius=0.5, width=6.5, height=3.3).shift(DOWN)
        self.play(Write(turing), Create(turing_rect))

        box = Group(group, turing, turing_rect)
        return box

    def highlight(self, current_rect, group):
        filled_rect = current_rect.copy()
        filled_rect.set_opacity(0.5)
        filled_rect.set_fill(BLUE_E)
        self.play(Transform(current_rect, filled_rect))
        self.wait()

        box = Group(filled_rect, group)
        return box

class Circuits(Scene):
    def construct(self):
        bg = ImageMobject("..\\..\\..\\assets\\manim_bg.png")
        self.add(bg)
        computer = ImageMobject("..\\..\\..\\assets\\computer-avatar.png").scale(0.5)
        self.add(computer)
        self.defining_computation()
        self.binary()

    def defining_computation(self):
        title = Text("Defining Computation", font="Oxygen", color=TITLE_COLOR)
        title.shift(UP * 3)
        self.play(Write(title), Write(Underline(title)))

    def binary(self):
        binary_steam1 = Text("010101101000011010111001010001101011110101010101011101010101011101010001")
        binary_steam2 = Text("010101101000011010111001010001101011110101010101011101010101011101010001")
        binary_steam3 = Text("010101101000011010111001010001101011110101010101011101010101011101010001")
